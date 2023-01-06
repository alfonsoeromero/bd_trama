#!/bin/sh
cd /Users/maria/work/bd_trama
source venv/bin/activate
python manage.py runserver &
sleep 3
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --kiosk http://127.0.0.1:8000/trama/
