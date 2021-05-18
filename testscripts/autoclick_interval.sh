#!/usr/bin/env bash
set -euo pipefail

while true
do
    adb shell input tap  80 135
    sleep 60
done
