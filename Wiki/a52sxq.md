# Installation Guide — Samsung Galaxy A52s 5G (a52sxq)

> [!WARNING]
> - Your warranty is void.
> - All official release builds are tested and safe to use.
> - If you decide to experiment, mess something up, corrupt your storage, turn your phone into a fancy paperweight, or brick it beyond recovery — **don’t blame us**.
> - You are doing this at **your own risk** and take full responsibility for anything that may happen.

> [!NOTE]
> - The device must have an **unlocked bootloader** and a **recommended custom recovery**.
> - Make sure to be on [latest](https://developer.android.com/tools/releases/platform-tools) **platform tools** for adb/fastboot commands.
> - Make a **full data backup** before flashing.
> - Ensure your device has at least **30% battery**.
> - Flash **only** files meant for **Samsung Galaxy A52s 5G (a52sxq)**.
> - First boot may take 5–10 minutes. Do **not** interrupt or force reboot unless it exceeds 10 minutes.

---

## Clean Installation

1. Boot into your **custom recovery**.
2. Select **Wipe → Format Data** and type `yes`.
3. Select **Advanced → ADB Sideload → Swipe to Start Sideload**.
4. Sideload the rom using this command in powershell/terminal:

```
adb sideload <drag-&-drop-rom.zip>
```
5. Go back to your recovery's main page.
6. *If you are using the **vanilla build**, flash **GApps** now.* *If you are using the **GMS build**, skip this step.*
7. Reboot back into **Recovery**.
8. Select **Wipe → Format Data** and type `yes`.
9. Reboot to **System**. 

---

## Update (Dirty Flash)

> [!NOTE]
> Dirty flashing **will not work** for major Android version upgrades  
> (example: **1.x → 2.x**).

### Method 1: OTA Update

1. Go to **Settings → System → System updates**.
2. Download the latest available build.
3. Tap **Reboot** once the download finishes.
4. The device will reboot into recovery and install the update.
6. Reboot to **System**.

---

### Method 2: Recovery Flash with downloaded rom.zip

1. Reboot to **Recovery**.
2. Select **Install → Choose ROM → Swipe to flash**.
3. Reboot to **System**.

---

### Method 3: Recovery Flash with ADB sideload
1. Reboot to **Recovery**.
2. Select **Advanced → ADB Sideload → Swipe to Start Sideload**.
3. Sideload the rom using this command in powershell/terminal:

```
adb sideload <drag-&-drop-rom.zip>
```
4. Go back to your recovery's main page.
5. *If you are using the **vanilla build**, flash **GApps** now.* *If you are using the **GMS build**, skip this step.*
6. Reboot to **System**.

---

> [!IMPORTANT]
> For **vanilla builds**, **GApps must be reflashed after every update**,  
> including **OTA** and **recovery-based dirty flashes**.

---

## Support / Bug Reports

📢 **[Telegram Group](https://t.me/+XP1c6dUf7yM4NmE1)** 
