#!/usr/bin/env python
from ppadb.client import Client as AdbClient
import time

# connect to adb server
client = AdbClient(host="127.0.0.1", port=5037)

# Connect to phone with wifi
device = client.device("192.168.0.12:5555")

while True:
    # Get foreground app name
    foreground_app = device.shell("dumpsys activity recents | grep 'Recent #0' | cut -d= -f2 | sed 's| .*||' | cut -d '/' -f1")
    timestamp = time.asctime(time.localtime())
    if foreground_app.strip() == "com.shopopop":
        device.shell("input tap 80 135") # Reload the page
        print(f"{timestamp} - On app - Reloaded")
        time.sleep(60)
    else:
        print(f"{timestamp} - Not on app")
        time.sleep(5)
