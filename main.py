#!/usr/bin/env python3
# /etc/kernel/install.d/95-uki-addons.install
# Kopieert /etc/uki-addons/*.addon.efi naast elke UKI.
import glob, os, shutil, sys

SRC = "/etc/uki-addons"

def log(msg: str):
    if os.environ.get("KERNEL_INSTALL_VERBOSE", "0") not in ("", "0"):
        print(f"95-uki-addons: {msg}", file=sys.stderr)

if len(sys.argv) < 3:
    log("Not enough command line arguments (need: command, kernel version)")
    sys.exit(0)

cmd, kver = sys.argv[1], sys.argv[2]
log(f"called with command={cmd!r} kver={kver!r}")

if os.environ.get("KERNEL_INSTALL_LAYOUT") != "uki":
    log(f"layout is {os.environ.get('KERNEL_INSTALL_LAYOUT')!r}, not 'uki' — skipping")
    sys.exit(0)

boot  = os.environ.get("KERNEL_INSTALL_BOOT_ROOT")
token = os.environ.get("KERNEL_INSTALL_ENTRY_TOKEN")
if not boot or not token:
    log(f"BOOT_ROOT={boot!r} ENTRY_TOKEN={token!r} — missing, skipping")
    sys.exit(0)

# Nieuwere systemd zet ENTRY_NAME; anders "<token>-<kver>" (zonder boot-teller)
name = os.environ.get("KERNEL_INSTALL_ENTRY_NAME") or f"{token}-{kver}"
dest = os.path.join(boot, "EFI", "Linux", f"{name}.efi.extra.d")
log(f"target directory: {dest}")

if cmd == "add":
    addons = sorted(glob.glob(os.path.join(SRC, "*.addon.efi")))
    log(f"found {len(addons)} addon(s) in {SRC}")
    if addons:
        os.makedirs(dest, exist_ok=True)
        log(f"created/ensured {dest}")
        for f in addons:
            target = os.path.join(dest, os.path.basename(f))
            log(f"copy {f} -> {target}")
            shutil.copyfile(f, target)   # ESP is FAT: geen rechten kopiëren
        log(f"copied {len(addons)} addon(s)")
    else:
        log("no addons to install")
elif cmd == "remove":
    log(f"removing {dest}")
    shutil.rmtree(dest, ignore_errors=True)
    log("remove done")
else:
    log(f"unknown command {cmd!r}, ignoring")

sys.exit(0)