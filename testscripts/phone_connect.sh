#!/usr/bin/env bash
#set -euo pipefail

# If the conn won't work, connect the phone by usb and run this command (open phone port)
adb tcpip 5555

# Connect with ADB to the phone
adb connect 192.168.1.12:5555

# Start session
scrcpy
