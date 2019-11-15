# **Django Application**
### How to install
    1. Install Python 3.x
    2. Create a virtual env
    3. Execute in the virtual env:
        3.1. ``pip install requirements.tx``
    4. Install PostgresSQL
    5. Create a postgres user 'udit' with password 'udit'
    6. Create a postgres database 'mistay'
### How to run
    1. Activate virtual env
    2. Execute:
        2.1. `python manage.py makemigrations`
        2.2. `python manage.py migrate`
        2.3. `python manage.py runserver`

    The application is now accessible from localhost:8000

### Endpoints
    1. localhost:8000/admin/
        1.1 This endpoint will help in accessing admin portal of the django application. <br>
            You need to create a superuser by the command, `python manage.py createsuperuser` to login into the admin portal.
    2. localhost:8000/events/
        2.1. localhost:8000/events/add/
        2.2. localhost:8000/events/delete/<event>
        2.3. localhost:8000/events/list/pk
        2.4. localhost:8000/events/register/<user>/<event>
        2.5. localhost:8000/events/unregister/<user>/<event>