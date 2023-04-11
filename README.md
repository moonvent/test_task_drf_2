Test task with DRF, test task reqs - https://teletype.in/@gimntut/mdo-test-drf#gdLt

All project requirements:
- for pip: requirements.txt
- for poetry: pyproject.toml

For startup project [Linux / MacOS] and test it:

For pip:
    1) cd tt_drf/djangoProject/
    2) virtualenv venv
    3) . venv/bin/activate
    4) pip intall -r requirements.txt
    5) python manage.py makemigration 
    6) python manage.py migrate 
    7) python manage.py createsuperuser 
    - admin
    - admin@admin.com
    - admin
    - admin
    - y
    8) python manage.py runserver 8000

Swagger on url: http://127.0.0.1:8000/schema/swagger-ui/
DRF api viewer: http://127.0.0.1:8000/api/entity/, admin panel data: login - admin, password - admin


