# **Events Application**
### How to install
    1. Install Python 3.x
    2. Create a virtual env
    3. Execute in the virtual env:
        3.1. pip install requirements.tx
    4. Install PostgresSQL
    5. Create a postgres user 'udit' with password 'udit'
    6. Create a postgres database 'mistay'
### How to run
    1. Activate virtual env
    2. Execute:
        2.1. python manage.py makemigrations
        2.2. python manage.py migrate
        2.3. python manage.py runserver

    The application is now accessible from localhost:8000

### Endpoints
    1. localhost:8000/admin/
        1.1 This endpoint will help in accessing admin portal of the django application.
            You need to create a superuser by the command, python manage.py createsuperuser to login into the admin portal.
    2. localhost:8000/events/
        2.1. localhost:8000/events/add/
            2.1.1. Type of request:
                    POST
            2.1.2. Data in body:
                    {
                        	"start": str(python datetime obj),
	                        "end": str(python datetime obj),
	                        "max_attendees": int,
	                        "type": "Public" or "Private",
	                        "name": str,
	                        "invited":[list of str],
	                        "owner": str
                    }
             2.1.3. Return JSON:
                    {
                            "status": str,
                            "errors": str
                    }
        2.2. localhost:8000/events/delete/<event_id>/<user_id>
            2.2.1. Type of request:
                    GET
            2.2.2. Data in the body:
                    None
            2.2.3. Return JSON:
                    {
                            "status": str,
                            "errors": str
                    }
        2.3. localhost:8000/events/list/<user_id>:
            2.3.1. Type of request:
                    GET
            2.3.2. Data in the body:
                    None
            2.3.3. Return JSON:
                    {
                        "data":
                                {
                                    "start": str (python datetime obj),
                                    "end": str (python datetime obj),
                                    "name": str,
                                    "type": "Public" or "Private",
                                    "max_attendees": int,
                                    "owner": int
                                }
                    }
        2.4. localhost:8000/events/register/<username>/<event_id>:
            2.4.1. Type of request:
                    GET
            2.4.2. Data in the body:
                    None
            2.4.3. Return JSON:
                    {
                        "status": str,
                        "errors": str
                    }
        2.5. localhost:8000/events/unregister/<username>/<event_id>:
            2.5.1. Type of request:
                    GET
            2.5.2. Data in the body:
                    None
            2.5.3. Return JSON:
                    {
                        "status": str,
                        "errors": str
                    }