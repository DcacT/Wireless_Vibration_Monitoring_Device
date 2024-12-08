@echo off
python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    pause
    exit /b
)

if exist requirements.txt (
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
)
if not exist "data/raw" (
    mkdir "data/raw"
    echo Folder "data/raw" created.
) else (
    echo Folder "data/raw" already exists.
)

:: Check and create folder "b"
if not exist "data/reports" (
    mkdir "data/reports"
    echo Folder "data/reports" created.
) else (
    echo Folder "data/reports" already exists.
)
start cmd /k "python visualizer.py"
start cmd /k "python bt_receiver.py"
pause
