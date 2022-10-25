#!/bin/sh
cd /Users/aeromero/work/projects/bd_trama
source venv/bin/activate
python manage.py runserver &
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --kiosk http://127.0.0.1:8000/trama/
