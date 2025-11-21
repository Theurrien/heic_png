@echo off
REM ================================================
REM HEIC to PNG Converter - Drag and Drop
REM ================================================
REM
REM Usage: Drag and drop HEIC files or folders onto this batch file
REM The converted PNG files will be created in the same location
REM

setlocal enabledelayedexpansion

echo ================================================
echo HEIC to PNG Converter
echo ================================================
echo.

REM Check if any files/folders were dropped
if "%~1"=="" (
    echo No files or folders were provided!
    echo.
    echo Usage:
    echo   1. Drag and drop HEIC files onto this batch file
    echo   2. Or drag and drop a folder containing HEIC files
    echo.
    pause
    exit /b 1
)

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo.
    echo Please run install_windows.bat first!
    echo.
    pause
    exit /b 1
)

REM Process each dropped item
:process_loop
if "%~1"=="" goto done

set "item=%~1"
echo Processing: %item%

REM Check if it's a directory
if exist "%item%\*" (
    echo Converting all HEIC files in directory...
    python "%~dp0heic_to_png.py" -d "%item%" -v
) else (
    REM It's a file
    echo Converting file...
    python "%~dp0heic_to_png.py" "%item%" -v
)

echo.
shift
goto process_loop

:done
echo ================================================
echo Conversion complete!
echo ================================================
echo.
echo Check the same folder(s) for your PNG files.
echo.
pause
