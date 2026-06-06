import argparse
import re
import sys

import generate

CONTROL_PATTERN = re.compile(r"[\x00-\x1f\x7f]")
CODENAME_PATTERN = re.compile(r"^[A-Za-z0-9_]+$")
DEVICE_PATTERN = re.compile(r"^(.+?)\s*\(([^()]+)\)\s*$")
GITHUB_PATTERN = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?$")
BLOCKED_MAINTAINER_ID_CHARS = frozenset("#\\%")


def parse_args():
    parser = argparse.ArgumentParser(description="Add a maintainer and device to the official registry.")
    parser.add_argument("--maintainer-id", required=True, help="Build-time AXION_MAINTAINER value")
    parser.add_argument("--maintainer-name", required=True, help="Public maintainer display name")
    parser.add_argument("--github", required=True, help="GitHub username or profile URL")
    parser.add_argument("--device", help="Device name and codename, for example: Google Pixel 9 Pro XL (komodo)")
    parser.add_argument("--device-name", help="Public device name")
    parser.add_argument("--codename", help="Device codename")
    parser.add_argument("--co-maintainer-id", action="append", default=[], help="Additional existing maintainer ID")
    parser.add_argument("--support-group", default="", help="Device support group URL")
    parser.add_argument("--image-url", default="", help="Fallback device image URL")
    parser.add_argument("--status", choices=("active", "inactive"), default="active")
    parser.add_argument("--unofficial", action="store_true", help="Add the device to the website but not official build detection")
    parser.add_argument("--hide-website", action="store_true", help="Keep the device out of website APIs")
    parser.add_argument("--dry-run", action="store_true", help="Validate and print the change without writing files")
    return parser.parse_args()


def clean(value, field, allow_empty=False):
    if value is None:
        if allow_empty:
            return ""
        raise ValueError(f"{field} is required")
    cleaned = value.strip()
    if not cleaned and not allow_empty:
        raise ValueError(f"{field} is required")
    if CONTROL_PATTERN.search(cleaned):
        raise ValueError(f"{field} contains control characters")
    return cleaned


def normalize_github(value):
    github = clean(value, "github")
    github = github.removeprefix("https://github.com/").removeprefix("http://github.com/").strip("/")
    if "/" in github:
        raise ValueError("github must be a username or profile URL")
    if not GITHUB_PATTERN.fullmatch(github):
        raise ValueError(f"invalid GitHub username {github}")
    return github


def normalize_maintainer_id(value):
    maintainer_id = clean(value, "maintainer-id")
    if any(char.isspace() for char in maintainer_id):
        raise ValueError("maintainer-id cannot contain whitespace")
    blocked = sorted(set(maintainer_id) & BLOCKED_MAINTAINER_ID_CHARS)
    if blocked:
        raise ValueError(f"maintainer-id contains unsupported character(s): {' '.join(blocked)}")
    return maintainer_id


def normalize_device(args):
    device_name = args.device_name
    codename = args.codename
    if args.device:
        match = DEVICE_PATTERN.fullmatch(clean(args.device, "device"))
        if not match:
            raise ValueError("device must look like: Device Name (codename)")
        parsed_name, parsed_codename = match.groups()
        if device_name and clean(device_name, "device-name") != parsed_name.strip():
            raise ValueError("device and device-name disagree")
        if codename and clean(codename, "codename") != parsed_codename.strip():
            raise ValueError("device and codename disagree")
        device_name = parsed_name
        codename = parsed_codename

    device_name = clean(device_name, "device-name")
    codename = clean(codename, "codename")
    if not CODENAME_PATTERN.fullmatch(codename):
        raise ValueError("codename can only contain letters, numbers, and underscores")
    return device_name, codename


def unique_maintainer_ids(primary, extra):
    values = [primary, *[normalize_maintainer_id(value) for value in extra]]
    return list(dict.fromkeys(values))


def registry_indexes(registry):
    maintainers = {maintainer["id"]: maintainer for maintainer in registry["maintainers"]}
    devices = {device["codename"]: device for device in registry["devices"]}
    devices_lower = {device["codename"].lower(): device for device in registry["devices"]}
    return maintainers, devices, devices_lower


def ensure_maintainer(registry, maintainer_id, name, github):
    maintainers, _, _ = registry_indexes(registry)
    existing = maintainers.get(maintainer_id)
    if existing:
        if existing["name"] != name:
            raise ValueError(f"maintainer {maintainer_id} already uses name {existing['name']}")
        if existing["github_username"] != github:
            raise ValueError(f"maintainer {maintainer_id} already uses GitHub {existing['github_username']}")
        return False

    registry["maintainers"].append({
        "id": maintainer_id,
        "name": name,
        "github_username": github,
    })
    return True


def add_device(registry, args, codename, device_name, maintainer_ids):
    maintainers, devices, devices_lower = registry_indexes(registry)
    if codename in devices or codename.lower() in devices_lower:
        raise ValueError(f"device {codename} already exists")
    for maintainer_id in maintainer_ids:
        if maintainer_id not in maintainers:
            raise ValueError(f"unknown co-maintainer {maintainer_id}")

    device = {
        "codename": codename,
        "name": device_name,
        "maintainers": maintainer_ids,
    }
    if args.status != "active":
        device["status"] = args.status
    if args.unofficial:
        device["official"] = False
    if args.hide_website:
        device["website"] = False
    support_group = clean(args.support_group, "support-group", allow_empty=True)
    image_url = clean(args.image_url, "image-url", allow_empty=True)
    if support_group:
        device["support_group"] = support_group
    if image_url:
        device["image_url"] = image_url
    registry["devices"].append(device)
    registry["devices"] = generate.sorted_devices(registry["devices"])
    return device


def print_summary(maintainer_added, device, dry_run):
    mode = "validated" if dry_run else "added"
    maintainer_mode = "new maintainer" if maintainer_added else "existing maintainer"
    print(f"{mode}: {device['codename']} / {device['name']} ({maintainer_mode})")
    print(f"official={str(generate.is_official(device)).lower()} website={str(generate.is_visible(device)).lower()} status={generate.device_status(device)}")
    print(f"maintainers={','.join(device['maintainers'])}")


def main():
    args = parse_args()
    try:
        maintainer_id = normalize_maintainer_id(args.maintainer_id)
        name = clean(args.maintainer_name, "maintainer-name")
        github = normalize_github(args.github)
        device_name, codename = normalize_device(args)
        registry = generate.load_registry()
        maintainer_added = ensure_maintainer(registry, maintainer_id, name, github)
        maintainer_ids = unique_maintainer_ids(maintainer_id, args.co_maintainer_id)
        device = add_device(registry, args, codename, device_name, maintainer_ids)
        generate.validate_registry(registry)
        if not args.dry_run:
            generate.generate_all(registry)
        print_summary(maintainer_added, device, args.dry_run)
    except Exception as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
