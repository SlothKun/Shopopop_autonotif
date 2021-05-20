#!/usr/bin/env python
from ppadb.client import Client as AdbClient
import time

def Get_timestamp():
    return time.asctime(time.localtime())

def Get_foregroundapp(device):
    return device.shell("dumpsys activity recents | grep 'Recent #0' | cut -d= -f2 | sed 's| .*||' | cut -d '/' -f1").strip()


# connect to adb server
client = AdbClient(host="127.0.0.1", port=5037)

# Connect to phone with wifi
device = client.device("192.168.1.12:5555")


result = device.screencap()

with open("testscreen.jpg", "wb") as fp:
	fp.write(result)
