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

## Useful links to liblaries what was used in that project
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

TODO: 
- finish User model
- add photos model
- finish api endpoints, validation, error codes (Modify user, get user, get user email, get/set profile photo, get register date or just get all)
- refactor, docstring, pep formatting
- some tests if time allows

OPTIONAL:
- cloud deploy
- try serverless (zappa, s3 aws for photos, aws postgres and lambda)
- docker local enviroment (fastest and easier to start env)