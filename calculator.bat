@echo off
setlocal enabledelayedexpansion

echo Welcome to the Calculator!

:menu
echo Choose an operation:
echo 1. Addition
echo 2. Subtraction
echo 3. Multiplication
echo 4. Division
echo 5. Exit

set /p "choice=Enter a number from the menu: "

if "%choice%"=="1" goto add
if "%choice%"=="2" goto subtract
if "%choice%"=="3" goto multiply
if "%choice%"=="4" goto divide
if "%choice%"=="5" goto exit

:add
set /p "num1=Enter the first number: "
set /p "num2=Enter the second number: "
set /a "result=num1 + num2"
echo The result: !result!
goto menu

:subtract
set /p "num1=Enter the first number: "
set /p "num2=Enter the second number: "
set /a "result=num1 - num2"
echo The result: !result!
goto menu

:multiply
set /p "num1=Enter the first number: "
set /p "num2=Enter the second number: "
set /a "result=num1 * num2"
echo The result: !result!
goto menu

:divide
set /p "num1=Enter the first number: "
set /p "num2=Enter the second number: "
if %num2% equ 0 (
    echo Error: Division by zero is not possible!
) else (
    set /a "result=num1 / num2"
    echo The result: !result!
)
goto menu

:exit
echo Exiting...
