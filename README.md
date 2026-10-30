# PyInstallScriptDTBO

## Install script
```sh
sudo install.sh
```
### Result

```bash
lennard@fedoraHP:/home/lennard/Documenten/School/BedrijfsProject_IOT/PyInstallScriptDTBO git:(main) $ sudo ./install.sh                              
+ install -m 755 95-uki-optional-addons.install /etc/kernel/install.d/
+ echo layout=uki
+ tee -a /etc/kernel/install.conf
lennard@fedoraHP:/home/lennard/Documenten/School/BedrijfsProject_IOT/PyInstallScriptDTBO git:(main) $ 
```

## testing script
```sh
sudo test.sh
```
### Result

```bash
lennard@fedoraHP:/home/lennard/Documenten/School/BedrijfsProject_IOT/PyInstallScriptDTBO git:(main) $ sudo ./test.sh                                 
+ ukify build --output=/tmp/dummy.addon.efi
Wrote unsigned /tmp/dummy.addon.efi
++ uname -r
+ KVER=7.2.12-200.fc44.x86_64
+ KERNEL_IMAGE=/usr/lib/modules/7.2.12-200.fc44.x86_64/vmlinuz
+ SRC_DIR=/usr/lib/modules/7.2.12-200.fc44.x86_64/vmlinuz.extra.optional.d
+ mkdir -p /usr/lib/modules/7.2.12-200.fc44.x86_64/vmlinuz.extra.optional.d
+ cp /tmp/dummy.addon.efi /usr/lib/modules/7.2.12-200.fc44.x86_64/vmlinuz.extra.optional.d/
+ rm /etc/kernel/uki-optional-addons
+ echo dummy.addon.efi
+ echo ontbreekt.addon.efi
+ kernel-install add
Kernel version not specified, starting autodetection 😖.
Found uname version: 7.2.12-200.fc44.x86_64
/var/tmp/dracut.dLinpXW/uefi/uki.sbat does not contain a valid SBAT section, skipping.
Wrote unsigned /var/tmp/dracut.dLinpXW/uefi/linux.efi
Using config file: /usr/lib/kernel/uki.conf
Wrote unsigned /var/tmp/kernel-install.staging.KSAOWY/uki.efi
DEBUG:__main__:Add command word uitgevoerd
DEBUG:__main__:/usr/lib/modules/7.2.12-200.fc44.x86_64/vmlinuz.extra.optional.d/dummy.addon.efi -> /boot/efi/EFI/Linux/42c0fb1acfbd4bbc86ce44ea94d46a17-7.2.12-200.fc44.x86_64.efi.extra.d/dummy.addon.efi
ERROR:__main__:'ontbreekt.addon.efi' staat in de lijst /etc/kernel/uki-optional-addons maar niet in /usr/lib/modules/7.2.12-200.fc44.x86_64/vmlinuz.extra.optional.d
lennard@fedoraHP:/home/lennard/Documenten/School/BedrijfsProject_IOT/PyInstallScriptDTBO git:(main) $ 
```