@echo off
echo Enabling High-Performance Mode...
adb shell settings put system screen_brightness_mode 0
adb shell settings put system screen_brightness 0
adb shell settings put system stay_on_while_plugged_in 3
echo High-Performance Mode has been enabled