@echo off
echo Limiting background processes...
.\adb\adb.exe shell settings put global limit_background_processes 1
if %errorlevel% neq 0 (
    echo Error: Limiting background processes failed.
) else (
    echo Success: Limiting background processes.
)
