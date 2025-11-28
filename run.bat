@echo off
echo ========================================
echo Shape Classification CNN - Quick Run
echo ========================================
echo.

REM Check if model exists
if exist drawing_classification.keras (
    echo Model found! Running predictions...
    echo.
    python predict.py --testdata
) else (
    echo Model not found. Training model first...
    echo.
    python cnn.py
    echo.
    echo Training complete! Now running predictions...
    echo.
    python predict.py --testdata
)

pause


