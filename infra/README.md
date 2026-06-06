# Official device registry

`infra/device_registry.json` is the source of truth for official devices, maintainer ownership, and website device metadata.

Generated outputs:

- `infra/official_devices.mk`: build-side device-to-maintainer allowlist
- `OTA/axion.devices`: legacy official device list
- `OTA/axion.maintainers`: legacy official maintainer list
- `api/downloads.json`: website device index with direct OTA JSON sources
- `api/maintainers.json`: public maintainer profile index
- `README.md`: supported-device and maintainer lists

Onboard a new maintainer/device with validation:

```bash
python3 infra/maintainer_onboarding.py \
  --maintainer-id ExampleMaintainer \
  --maintainer-name "Example Maintainer" \
  --github https://github.com/example \
  --device "Example Phone (example)" \
  --support-group https://t.me/example \
  --image-url https://example.com/device.png
```

Use `--dry-run` to validate without writing. The script rejects whitespace in maintainer IDs, mismatched existing maintainer data, duplicate codenames, invalid GitHub usernames, and unknown co-maintainers. Generated official-device outputs are sorted automatically by brand, device name, and codename. Default `active`, official, and website-visible fields are omitted from the registry to keep the source of truth compact.

After hand-editing the registry, run:

```bash
python3 infra/generate.py
```

Existing-device download links come directly from `OTA/GMS/<codename>.json` and `OTA/VANILLA/<codename>.json`; updating those OTA files does not require copying download data into another API file.
