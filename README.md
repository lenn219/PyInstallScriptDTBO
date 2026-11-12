# PyInstallScriptDTBO

## How does it work

This plugin gets trigger by the kernel install and then we pick it up from there.

On `kernel-install add` it:

1. Checks that `KERNEL_INSTALL_LAYOUT=uki`
2. Reads the list of desired add-ons from `/etc/kernel/uki-optional-addons`
3. Copies each listed `.addon.efi` from  
   `/usr/lib/modules/<kernel>/vmlinuz.extra.optional.d/`  
   into  
   `$BOOT/EFI/Linux/<entry-token>-<kernel>.efi.extra.d/`

`systemd-stub` then loads those files at boot. **This does not run at boot time only when kernel-install add is run**

The plugin does nothing if the layout is not `uki` or if the list file is missing/empty.


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
lennard@fedoraHP:/home/lennard/Documenten/School/BedrijfsProject_IOT/PyInstallScriptDTBO git:(bashRewrite*) $ sudo ./test.sh 
allexport       off
braceexpand     on
emacs           off
errexit         on
errtrace        off
functrace       off
hashall         on
histexpand      off
history         off
ignoreeof       off
interactive-comments    on
keyword         off
monitor         off
noclobber       off
noexec          off
noglob          off
nolog           off
notify          off
nounset         on
onecmd          off
physical        off
pipefail        off
posix           on
privileged      off
verbose         off
vi              off
xtrace          off
+ rm /tmp/dummy.addon.efi
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
/var/tmp/dracut.dsKHUjQ/uefi/uki.sbat does not contain a valid SBAT section, skipping.
Wrote unsigned /var/tmp/dracut.dsKHUjQ/uefi/linux.efi
Using config file: /usr/lib/kernel/uki.conf
Wrote unsigned /var/tmp/kernel-install.staging.BRt4Gi/uki.efi
ERROR: 'ontbreekt.addon.efi' is listed in /etc/kernel/uki-optional-addons but missing in /usr/lib/modules/7.2.12-200.fc44.x86_64/vmlinuz.extra.optional.d
```
