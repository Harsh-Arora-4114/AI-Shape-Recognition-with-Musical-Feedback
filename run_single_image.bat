@echo off
echo ========================================
echo Shape Classification - Single Image
echo ========================================
echo.

if "%1"=="" (
    echo Usage: run_single_image.bat "path/to/image.png"
    echo Example: run_single_image.bat "shapes/test/circles/drawing(100).png"
    pause
    exit /b
)

python predict.py --image %1

pause


