@echo off

call %~dp0venv\Scripts\activate

cd %~dp0

set TOKEN=2074925896:AAG_T2yDKMCOEcpp0ZnOIfpT_J0E4B2ZBBQ

python goroskop_bot.py

pause