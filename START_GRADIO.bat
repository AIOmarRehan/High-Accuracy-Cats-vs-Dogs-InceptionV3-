@echo off
REM Cats vs Dogs Classifier - Gradio Launcher

echo.
echo =========================================
echo Cats vs Dogs Classifier - Gradio
echo =========================================
echo.

REM Check if Python 3.10 is installed
py -3.10 --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python 3.10 is not installed
    echo Please install Python 3.10
    pause
    exit /b 1
)

REM Check if Gradio is installed for Python 3.10
py -3.10 -c "import gradio" >nul 2>&1
if errorlevel 1 (
    echo Installing required packages for Python 3.10...
    py -3.10 -m pip install -r requirements.txt
)

echo.
echo Starting Gradio application using Python 3.10...
echo.
echo Once ready, open your browser at: http://localhost:7860
echo.

REM Launch the Gradio app with Python 3.10
py -3.10 run_gradio.py

pause