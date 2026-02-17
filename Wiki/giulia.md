# Installation Guide — Oneplus 13R (giulia)

> [!WARNING]
> - Your warranty is void.
> - All official release builds are tested and safe to use.
> - If you decide to experiment, mess something up, corrupt your storage, turn your phone into a fancy paperweight, or brick it beyond recovery — **don’t blame us**.
> - You are doing this at **your own risk** and take full responsibility for anything that may happen.

> [!NOTE]
> - The device must have an **unlocked bootloader**.
> - Ensure you have the **same firmware on both slots**. If you are coming from OOS/COS you can either use regional/super [flasher](https://github.com/yashaswee-exe/AndroidGuides/wiki/SuperFlasher-script-for-OP13R-%7C-Ace5) to flash oos/cos on both slots. If you are not comfortable with this, local install the current firmware version.
> - Make sure to be on [latest](https://developer.android.com/tools/releases/platform-tools) **platform tools** for adb/fastboot commands.
> - Make a **full data backup** before flashing.
> - Ensure your device has at least **30% battery**.
> - Flash **only** files meant for **Oneplus 13R (giulia)**.
> - First boot may take 5–10 minutes. Do **not** interrupt or force reboot unless it exceeds 10 minutes.

---

## Clean Installation

1. Download **latest rom.zip**.
2. Dump the zip through payload dumper using this [guide](https://xdaforums.com/t/guide-how-to-extract-img-boot-img-etc-from-payload-bin-using-payload-dumper-go.4468781/) and grab **boot, vendor_boot, init_boot, and recovery images**.
3. Connect your phone to PC and reboot to **fastboot** by holding both power button and volume down keys.
4. Flash the following partitions **one by one** through powershell/terminal using:

```
fastboot flash boot <drag-&-drop-boot.img>
```
```
fastboot flash vendor_boot <drag-&-drop-vendor_boot.img>
```
```
fastboot flash init_boot <drag-&-drop-init_boot.img>
```
```
fastboot flash recovery <drag-&-drop-recovery.img>
```
5. Reboot to **recovery** using:

```
fastboot reboot recovery
```
6. Select **Factory reset → Format data/factory reset**.
7. Select **Apply update → Apply from ADB**, then sideload the rom using:

```
adb sideload <drag-&-drop-rom.zip>
```
8. After sideload completes, select **YES** to reboot if you have extra packages (i.e., GApps) to install and **NO** if you have none.
9. Select **Factory reset → Format data/factory reset**.
10. Select **Reboot system now**.

---

## Update (Dirty Flash)

> [!NOTE]
> Dirty flashing **will not work** for major Android version upgrades  
> (example: **1.x → 2.x**).

### Method 1: OTA Update

1. Go to **Settings → System → System updates**.
2. Download the latest available build.
3. Tap **Reboot** once the download finishes.
4. The device will reboot and install the update.

---

### Method 2: Recovery Flash

1. Reboot to **Recovery**.
2. Select **Apply update → Apply from ADB**, then sideload the rom using:

```
adb sideload <drag-&-drop-rom.zip>
```
3. After sideload completes, select **YES** to reboot if you have extra packages (i.e., GApps) to install and **NO** if you have none.
4. Select **Reboot system now**.

---

> [!IMPORTANT]
> For **vanilla builds**, **GApps must be reflashed after every update**,  
> including **OTA** and **recovery-based dirty flashes**.

---

## Support / Bug Reports

📢 **[Telegram Group](https://t.me/+AjwuK7p-rJ44ZmU1)** 
