#!/usr/bin/env python
from ppadb.client import Client as AdbClient
import time

# connect to adb server
client = AdbClient(host="127.0.0.1", port=5037)

# Connect to phone via wifi
device = client.device("192.168.0.12:5555")

while True:
    device.shell("input tap 80 135")
    time.sleep(60)
