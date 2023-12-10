pip install -r requirements.txt
cls
@echo off
echo Diga 1 para escolher Pracas ou 2 para escolher Graduados
set /p choice=Escolha: 

if "%choice%"=="1" (
    python Pracas.py
) else if "%choice%"=="2" (
    python Graduados.py
) else (
    echo Escolha inválida. Por favor, escolha 1 ou 2.
)

pause
