# Setting Up OTA JSON and Adding a New Maintainer/Device

## OTA JSON Format

To setup updates, you need to provide a JSON file named after your device (e.g., device.json), following this structure:

```device.json
{
  "response": [
    {
      "datetime": 1230764400,
      "filename": "ota-package.zip",
      "id": "5eb63bbbe01eeed093cb22bb8f5acdc3", //md5
      "romtype": "OFFICIAL",
      "size": 314572800, // size in bytes
      "url": "https://example.com/ota-package.zip",
      "version": "1.1"
    }
  ]
}
```

### Attribute Details

| Attribute  | Description  |
|------------|-------------|
| `datetime`  | Build date as a UNIX timestamp.  |
| `filename`  | The name of the update package file.  |
| `id`  | A unique identifier for the update.  |
| `romtype`  | The release type (e.g., `OFFICIAL`), compared with `ro.lineage.releasetype`.  |
| `size`  | The update file size in bytes.  |
| `url`  | Direct URL to the update package.  |
| `version`  | The build version, compared with `ro.lineage.build.version`.  |

Ensure that the JSON file is hosted at an accessible URL and follows this format exactly to avoid update errors.

---

## Adding a New Maintainer & Device

Each device must be registered in `infra/device_registry.json` with its correct codename and assigned maintainer ID. Generated lists and APIs come from that registry.

### Requirements:

- **Device Codename**: Must match the official device codename (e.g., `Pixel 6` → `oriole`).
- **Maintainer ID**: Must match the `AXION_MAINTAINER` string defined in the build environment.

### Steps to Add a Device:

1. **Run** `python3 infra/maintainer_onboarding.py --dry-run ...` with the maintainer ID, GitHub profile, device name, and codename.
2. **Run** the same command without `--dry-run` after validation passes.
3. **Ensure the maintainer ID** is correctly set in `AXION_MAINTAINER`.
4. **Add or update OTA JSON** under `OTA/GMS` and/or `OTA/VANILLA`.
5. **Run** `python3 infra/generate.py` after registry changes. Existing-device OTA JSON updates are read directly by the website and do not need download data copied elsewhere.
6. **Push changes** with the registry, OTA JSON, and generated outputs.
