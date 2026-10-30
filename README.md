# PyInstallScriptDTBO

The install script is used to read the [/usr/lib/modules/uki.extra.d](https://uapi-group.org/specifications/specs/unified_kernel_image/) and place these in the boot file system so that systemd-stub can use it to boot with changes to the DTBO or simulair.

```bash
sudo kernel-install add $(uname -r) /lib/modules/$(uname -r)/vmlinuz -v
```