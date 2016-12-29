@echo off

IF NOT EXIST venv (virtualenv venv)
call venv/scripts/activate.bat
pip install -r requirements.txt

