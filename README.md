##  Start app locally
Run local enviroment (I used mkvirtualenv in that case)
```
mkvirtualenv excedo -p python3.6
pip install -r requirements.txt
```

Export configuration
```
export APP_SETTINGS="config.DevelopmentConfig"
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

## Useful links
```
http://flask-sqlalchemy.pocoo.org/2.3/
https://flask-migrate.readthedocs.io/en/latest/
https://flask-restful.readthedocs.io/en/latest/quickstart.html#
```

TODO: debug mode not working? check config class and os env get