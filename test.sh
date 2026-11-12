#!/usr/bin/env sh
# dit moet als root gedraaid worden.
# Dit is om te voorkomen dat als er iets faalt dat de script door gaat.
set -euo 
set -x          # optioneel: debug (print elke command)


rm /tmp/dummy.addon.efi

ukify build --output=/tmp/dummy.addon.efi

KVER=$(uname -r)

# KERNEL_IMAGE="/usr/lib/modules/${KVER}"
KERNEL_IMAGE="/usr/lib/modules/${KVER}/vmlinuz"

SRC_DIR="${KERNEL_IMAGE}.extra.optional.d"

# plaats de dummy in de locatie
mkdir -p "$SRC_DIR"
cp /tmp/dummy.addon.efi "$SRC_DIR/"

rm /etc/kernel/uki-optional-addons
echo "dummy.addon.efi" >> /etc/kernel/uki-optional-addons
echo "ontbreekt.addon.efi" >> /etc/kernel/uki-optional-addons


kernel-install add
