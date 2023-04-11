Test task with DRF, test task reqs - https://teletype.in/@gimntut/mdo-test-drf#gdLt

All project requirements:
- for pip: requirements.txt
- for poetry: pyproject.toml

For startup project [Linux / MacOS] and test it:

For pip:

    cd tt_drf/djangoProject/
    virtualenv venv
    . venv/bin/activate
    pip intall -r requirements.txt
    python manage.py makemigration
    python manage.py migrate
    python manage.py createsuperuser
    - admin
    - admin@admin.com
    - admin
    - admin
    - y
    python manage.py runserver 8000

Swagger on url: http://127.0.0.1:8000/schema/swagger-ui/
DRF api viewer: http://127.0.0.1:8000/api/entity/, admin panel data: login - admin, password - admin


