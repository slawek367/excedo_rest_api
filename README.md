##  Start app locally
Run local enviroment (I used mkvirtualenv in that case)
```
mkvirtualenv excedo -p python3.6
pip install -r requirements.txt
```

Export configuration
```
export FLASK_ENV=development
```
Start server
```
flask run --host=0.0.0.0
```

## Database configuration
Install postgresql
```
https://tecadmin.net/install-postgresql-server-on-ubuntu/
```

Run psql console and create db
```
sudo su - postgres
psql
postgres=# CREATE USER slawek SUPERUSER;
postgres=# CREATE DATABASE excedo_db WITH OWNER slawek;
\q
```
Where i used "slawek" you can use your username

Make migrations
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py db --help
```

Check if tables was created
```
sudo su - postgres
psql
\c excedo_db
\dt
```

External db
```
export DATABASE_URL=db_url
```

## Useful links
```
http://flask-sqlalchemy.pocoo.org/2.3/
https://flask-migrate.readthedocs.io/en/latest/
https://flask-restful.readthedocs.io/en/latest/quickstart.html#
```

TODO: 
- debug mode not working? check config class and os env get
- finish User model
- add photos model
- finish api endpoints, validation, error codes (Modify user, get user, get user email, get/set profile photo, get register date or just get all)
- refactor, docstring, pep formatting
- some tests if time allows

OPTIONAL:
- cloud deploy
- try serverless (zappa, s3 aws for photos, aws postgres and lambda)
- docker local enviroment (fastest and easier to start env)