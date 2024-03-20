from ykman.device import list_all_devices
from yubikit.core.smartcard import SmartCardConnection
import time

for device, info in list_all_devices():
    if info.version >= (5, 0, 0):
        print(f"YubiKey Serial Number Detected: {info.serial}")
    time.sleep(30) 
