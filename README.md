# PyInstallScriptDTBO

The install script is used to read the [/usr/lib/modules/uki.extra.d](https://uapi-group.org/specifications/specs/unified_kernel_image/) and place these in the boot file system so that systemd-stub can use it to boot with changes to the DTBO or simulair.

```bash
sudo KERNEL_INSTALL_VERBOSE=1 \
     KERNEL_INSTALL_LAYOUT=uki \
     KERNEL_INSTALL_BOOT_ROOT=/boot \
     KERNEL_INSTALL_ENTRY_TOKEN=machineid \
     /etc/kernel/install.d/95-uki-addons.install add $(uname -r)
```