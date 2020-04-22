#!/usr/bin/env python3
import os
import shutil
import sys

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def check_disk_usage(disk, min_absolute, min_percent):
    """This will return True if there is enough free disk space, False otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_absolute:
        return False
    return True

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    print("Everything ok.")
    sys.exit(0)

main()
