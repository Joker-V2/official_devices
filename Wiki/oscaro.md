# Installation Guide — OnePlus Nord CE2 Lite (oscaro)

> [!WARNING]
> - Your warranty is void.
> - All official release builds are tested and safe to use.
> - If you decide to experiment, mess something up, corrupt your storage, turn your phone into a fancy paperweight, or brick it beyond recovery — **don’t blame us**.
> - You are doing this at **your own risk** and take full responsibility for anything that may happen.

> [!NOTE]
> - The device must have an **unlocked bootloader** and a **recommended custom recovery**.
> - Make a **full data backup** before flashing.
> - Ensure your device has at least **30% battery**.
> - Flash **only** files meant for **OnePlus Nord CE2 Lite (oscaro)**.
> - First boot may take 5–10 minutes.Do **not** interrupt or force reboot unless it exceeds 10 minutes.

---

## Clean Installation

1. Boot into your **custom recovery**.
2. Go to **Wipe → Advanced Wipe**.
3. Select **Data, Dalvik, Cache**.
4. Flash the **ROM** *using sdcard/usb/sideload methods*.
5. *If you are using the **vanilla build**, flash **GApps** now.* *If you are using the **GMS build**, skip this step.*
6. If need to flash Gapps for vanilla or kernel, change slot respectively
7. Reboot back into **Recovery**.
8. Select **Wipe → Format Data** and type `yes`.
9. Reboot to **System**. 

---

## Update (Dirty Flash)

> [!NOTE]
> Dirty flashing **will not work** for major Android version upgrades  
> (example: **1.x → 2.x**).

### Method 1: OTA Update
**(Suitable for AOSP recovery users)**
1. Go to **Settings → System → System updates**.
2. Download the latest available build.
3. Tap **Install&Reboot** once the download finishes.
4. Reflash Gapps/kernel if necessary
---

### Method 2: Recovery Flash

1. Reboot to **Recovery**.
2. Select **Install → Choose ROM → Swipe to flash/Sideload**.
3. Wipe Dalvik/Cache
4. Reflash Gapps/kernel if necessary (Change slot is needed)
5. Reboot to **System**.

---

> [!IMPORTANT]
> For **vanilla builds**, **GApps must be reflashed after every update**,
> including **OTA** and **recovery-based dirty flashes**.

---

## Links to Necessary files
1. **[OrangeFox Recovery](https://t.me/oscaro_op/719)**
2. **[KSU Kernel](http://t.me/MissRose_bot?start=notes_-1002897540287_2091202)**

## Support / Bug Reports

📢 **[Telegram Group](https://t.me/oscaro_aosp)** 
