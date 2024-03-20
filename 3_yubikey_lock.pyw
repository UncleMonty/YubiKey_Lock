import os
import time
import ctypes
import subprocess
from ykman.device import list_all_devices

# Vendor and product ID for YubiKey
# found at https://support.yubico.com/hc/en-us/articles/360016614920-YubiKey-USB-ID-Values
YUBIKEY_VENDOR_ID = 0x1050 # Vendor is Yubico; this will remain unchanged
YUBIKEY_PRODUCT_ID = 0x0407 # Change this to your Product_ID - Example provided is: Yubikey 5 OTP+FIDO+CCID
EXPECTED_SERIAL_1 = int(12345678)  # Modify this to your desired expected serial number
# EXPECTED_SERIAL_2 = int(FILL_IN_SN)  # Uncomment this if you have additional Serial Numbers.
EXPECTED_USER = 'FILL IN USERNAME HERE'  # Modify this to your expected username

def find_yubikeys():
    # Find YubiKey device
    connected_serials = set()
    devices = list_all_devices()
    for device, info in devices:
        if info.serial:
            connected_serials.add(info.serial)
            # print(f"Detected YubiKey with serial: {info.serial}")
    return connected_serials

def get_current_username():
    # Use the getpass module to get the username
    try:
        username = os.getlogin()
        return username
    except OSError:
        print("Unable to retrieve the username.")
        return None

def lock_screen():
    # Lock the workstation
    ctypes.windll.user32.LockWorkStation()

def main():
    while True:
        connected_serials = find_yubikeys()
        username = get_current_username()
        if username is not None:
            if username == EXPECTED_USER and (EXPECTED_SERIAL_1 in connected_serials in connected_serials):
            # If you have another SN, uncomment the line below, and remove the or comment out the line above.
            # if username == EXPECTED_USER and (EXPECTED_SERIAL_1 in connected_serials or EXPECTED_SERIAL_2 in connected_serials):
                print(f"Authorized Yubikey and user detected, workstation remaining unlocked")
            else:
                print(f"User not authorized, or authorzied YubiKey not detected. Locking screen...")
                lock_screen()
        else:
            print("Error retrieving username. Exiting loop.")
        time.sleep(1)  # Check every 1 second

if __name__ == "__main__":
    # Detach the process to run windowless
    subprocess.Popen(["pythonw"], creationflags=subprocess.DETACHED_PROCESS, close_fds=True)
    main()
