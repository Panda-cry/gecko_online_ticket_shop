#flask run
flask db upgrade
gunicorn -w 4 "app:create_app()" -b 0.0.0.0:8000 --access-logfile=-



