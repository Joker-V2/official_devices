# Installation Guide — Xiaomi Mi 11T Pro (vili)

> [!WARNING]
> - Your warranty is void.
> - All official release builds are tested and safe to use.
> - If you decide to experiment, mess something up, corrupt your storage, turn your phone into a fancy paperweight, or brick it beyond recovery — **don’t blame us**.
> - You are doing this at **your own risk** and take full responsibility for anything that may happen.

> [!NOTE]
> - The device must have an **unlocked bootloader** and a **recommended custom recovery**.
> - Make a **full data backup** before flashing.
> - Ensure your device has at least **30% battery**.
> - Flash **only** files meant for **Xiaomi Mi 11T Pro (vili)**.
> - First boot may take 5–10 minutes.Do **not** interrupt or force reboot unless it exceeds 10 minutes.

---

### First time installation (clean flash):

* Unlock Bootloader
* Reboot Fastboot
* fastboot flash boot boot.img
* fastboot flash vendor_boot vendor_boot.img
* fastboot reboot recovery
* Now in recovery go to factory reset and confirm the reset
* Choose apply update and Apply from ADB
* Now install axion zip via sideload

```
adb sideload axion.zip
```
* When asked to sideload gapps, choose 'Yes' to reboot to recovery or 'No' if you don't want gapps and want to reboot to system
* Now if you choosed to install gapps, simply sideload gapps.zip the same way you installed axion.zip then reboot to system

---

### Update installation (Dirty Flash):
#### Via recovery (recommended way):
* Boot to recovery
* Choose apply update and Apply from ADB
* Now install axion zip via sideload and reboot
* If you had gapps, reboot to recovery and sideload gapps.zip and reboot

```
adb sideload axion.zip
```
---

#### Via OTA:
* Go to Settings -> System -> System updates and download latest build
* Choose install and let it finish
* If having gapps, reboot to recovery and sideload gapps package again
* Reboot

---

> [!IMPORTANT]
> For **vanilla builds**, **GApps must be reflashed after every update**,  
> including **OTA** and **recovery-based dirty flashes**.

---

## Support / Bug Reports

📢 **[Telegram Group](https://t.me/+d9Y_N7yuDpxkMmE1)** 
