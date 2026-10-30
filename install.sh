#!/usr/bin/sh
# Dit is om te voorkomen dat als er iets faalt dat de script door gaat.
set -euo pipefail
set -x          # optioneel: debug (print elke command)

# this Script is used to install the 95-uki-addons.install to the right folder.

# install is simply a copy but allows me to change attributes.
install -m 755 95-uki-addons.install /etc/kernel/install.d/


echo ./etc/kernel/install.conf | tee -a /etc/kernel/install.conf > /dev/null