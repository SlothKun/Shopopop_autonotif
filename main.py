#!/usr/bin/env python
from ppadb.client import Client as AdbClient
import time
import PIL.Image as Image


def Get_timestamp():
    return time.asctime(time.localtime())


def Get_foregroundapp(device):
    return device.shell("dumpsys activity recents | grep 'Recent #0' | cut -d= -f2 | sed 's| .*||' | cut -d '/' -f1").strip()


def Screen(device):
    with open("phonescreen.jpg", "wb") as fp:
        fp.write(device.screencap())


def Get_refreshcoordinates():
    img = Image.open('phonescreen.jpg')
    rgb_img = img.load()
    i = 1
    pixelstart = rgb_img[0,0]
    newpixel = rgb_img[0,i]

    while pixelstart == newpixel:
        newpixel = rgb_img[0,i]
        i += 1

    y = i - int(i/3)
    x = 1
    newpixel = rgb_img[0,y]

    try:
        while pixelstart == newpixel:
            newpixel = rgb_img[x,y]
            x += 1
        print(f"{Get_timestamp()} - On App - Refresh Button Found ({x},{y})")
        return (x,y)
    except Exception as e: # On other menus that the main one
        print(f"{Get_timestamp()} - On App - Refresh Button Not Found")
        return (-1,-1) # return coordinate error


def Get_checkdeliv():
    try:
        img = Image.open('phonescreen.jpg')
        rgb_img = img.load()

        x = int(im.size[0] / 2)
        y = int(im.size[1] / 2)

        target = (27, 63, 147)
        newpixel = rgb_img[x,y]

        while target != newpixel:
           newpixel = rgb_img[x,y]
           y += 1

        if rgb_img[x, y+1] == target and rgb_img[x, y+2] == target:
            print(f"{Get_timestamp()} - On App - Delivery Found")
            return True
    except Exception as e:
        print(f"{Get_timestamp()} - On App - No Delivery Found")
        return False
    

# Connect to adb server
client = AdbClient(host="127.0.0.1", port=5037)

# Connect to phone with wifi
device = client.device("192.168.1.12:5555")

"""
while True:
    # Get foreground app name
    foreground_app = device.shell("dumpsys activity recents | grep 'Recent #0' | cut -d= -f2 | sed 's| .*||' | cut -d '/' -f1")
    timestamp = time.asctime(time.localtime())
    if foreground_app.strip() == "com.shopopop":
        device.shell("input tap 80 135") # Reload the page
        print(f"{timestamp} - On App - Reloaded")
        time.sleep(60)
    else:
        print(f"{timestamp} - Not On App")
        time.sleep(5)
"""

while True:
    if Get_foregroundapp(device) == "com.shopopop":
        Screen(device)
        # Check if there's a refresh button & get its coordinates
        refreshcoordinates = Get_refreshcoordinates()
        if refreshcoordinates != (-1, -1) and Get_checkdeliv() == True:
            device.shell("cmd notification post -S bigtext -t 'NewDelivery'")
        device.shell(f"input tap {refreshcoordinates[0]} {refreshcoordinates[1]}")
        time.sleep(30)
    else:
        print(f"{Get_timestamp()} - Not On App")
        time.sleep(5)
