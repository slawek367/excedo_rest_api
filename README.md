# Excedo rest api

##  Start app locally
Create virtual enviroment (I used mkvirtualenv in that case with python 3.6 on ubuntu 16.04)
```
mkvirtualenv excedo -p python3.6
pip install -r requirements.txt
```

Export enviroment variable to start local server
```bash
export FLASK_ENV=development
```
Run server
```bash
flask run --host=0.0.0.0
```

## Database configuration
Install postgresql database
```
https://tecadmin.net/install-postgresql-server-on-ubuntu/
```

Run psql console and create db
```sql
sudo su - postgres
psql
postgres=# CREATE USER <your_username> SUPERUSER;
postgres=# CREATE DATABASE excedo_db WITH OWNER <your_username>;
\q
```

Make db migrations
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

Check if tables was created
```
sudo su - postgres
psql
\c excedo_db
\dt
```

To use external database for example PostgreSQL from AWS RDS export variable
```bash
export DATABASE_URL="postgres://<user>:<password>@<aws_url>:<port>/<db_name>"
```

##  Testing
Currently tests using local database which is hardcoded in config.py as LOCAL_DB_URL variable

Run integration flask rest api tests
```
pytest integration_tests.py -v
```

##  REST api endpoints

* GET `/users`

``` json
Returns list of users


[
    {
        "email": "test@o2.pl",
        "id": 1,
        "register_date": "2019-02-18 05:55:02",
        "username": "test1"
    }
]
```
* POST `/users`

```json
Mandatory fields

{
    "username": "test1",
    "password": "test123",
    "email": "test@o2.pl"
}
```
* GET `/users/{user_name}`
```
Return user data

{
    "email": "test@o2.pl",
    "id": 1,
    "register_date": "2019-02-18 05:55:02",
    "username": "test1"
}
```
* PUT `/users/{user_name}`
```
Update email

{
    "email": "test2@o2.pl"
}

Update password

{
    "old_password": "oldpass",
    "new_password": "newpass
}
```
* POST `/users/{user_name}/profile_photo`

    Upload profile photo with key "photo"
* GET `/users/{user_name}/profile_photo`

```
Return informations about user photo

{
    "id": 1,
    "url": "http://some_hosting_url_server.user_name_profile_photo.jpg",
    "user_id": 1
}
```

## Useful links to libraries what was used in that project
```
Flask
http://flask.pocoo.org/

Flask sqlalchemy
http://flask-sqlalchemy.pocoo.org/2.3/

Flask migrate
https://flask-migrate.readthedocs.io/en/latest/

Flask restful
https://flask-restful.readthedocs.io/en/latest/quickstart.html#

Testing
http://flask.pocoo.org/docs/1.0/testing/
```
