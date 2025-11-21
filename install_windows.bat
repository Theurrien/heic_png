@echo off
echo ================================================
echo HEIC to PNG Converter - Windows Installation
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo.
    echo Please install Python 3.7 or higher from:
    echo https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation!
    echo.
    pause
    exit /b 1
)

echo [OK] Python found:
python --version
echo.

REM Check if pip is available
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] pip is not available
    echo.
    echo Please reinstall Python with pip included
    echo.
    pause
    exit /b 1
)

echo [OK] pip found:
python -m pip --version
echo.

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip
echo.

REM Install requirements
echo Installing required packages...
echo This may take a few minutes...
echo.
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo [ERROR] Installation failed
    echo.
    echo Try running this command manually:
    echo python -m pip install -r requirements.txt
    echo.
    pause
    exit /b 1
)

echo.
echo ================================================
echo Installation completed successfully!
echo ================================================
echo.
echo You can now use the converter by running:
echo   heic_to_png.bat image.heic
echo.
echo Or with Python directly:
echo   python heic_to_png.py image.heic
echo.
echo For help, run:
echo   heic_to_png.bat --help
echo.
pause
