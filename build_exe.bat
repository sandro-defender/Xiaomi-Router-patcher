@echo off
chcp 65001 >NUL
SET PYTHONUNBUFFERED=TRUE

python build_exe.py --install-deps %*
if errorlevel 1 (
    echo Build failed.
    pause
    exit /b 1
)

echo.
echo Done. The executable is in dist\XMiR-Patcher\
pause
