@echo off
cd /d %~dp0

:: Display a welcome message
cls
echo =====================================================
echo             Python Environment Setup Tool
echo =====================================================
echo.
echo Press Enter to continue
pause >nul
echo.

:: Check if Python is installed
title Checking Python installation...
echo Checking Python installation...
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not added to PATH!
    echo.
    echo Please go to https://www.python.org/downloads and install the latest version.
    echo Make sure to check the option "Add Python to PATH" during installation.
    echo.
    goto ERROR
)

:: Check and install required libraries
title Checking libraries...
echo =====================================================
echo                  Checking Libraries
echo =====================================================
echo.

call :check_library customtkinter 1
call :check_library pillow 2
call :check_library pyaes 3
call :check_library urllib3 4
call :check_library PyQt5 5
call :check_library PyQtWebEngine 6
call :check_library colorama 7
call :check_library psutil 8
call :check_library keyboard 9
call :check_library requests 10
call :check_library dnspython 11
call :check_library selenium 12
call :check_library deep-translator 13
call :check_library phonenumbers 14
call :check_library bcrypt 15
call :check_library beautifulsoup4 16
call :check_library pypiwin32 17

:: Start the builder
cls
title Starting builder...
echo =====================================================
echo                   Starting Builder
echo =====================================================
echo.
python redtiger.py
if %errorlevel% neq 0 goto ERROR

echo =====================================================
echo               Builder started successfully
echo =====================================================
pause
exit

:check_library
    set "lib_name=%~1"
    set /a "lib_num=%~2"

    echo Checking '%lib_name%' (%lib_num%/17)
    python -c "import %lib_name%" > nul 2>&1
    if %errorlevel% neq 0 (
        echo Installing %lib_name%...
        python -m pip install %lib_name% > nul
    )
    echo.
    goto :eof

:ERROR
title [Error]
echo =====================================================
echo                       [Error]
echo =====================================================
echo An error occurred. Please check the messages above.
pause > nul
