import os
import tempfile
import pytest
import json
from app import app, db
from model.user import User
from config import LOCAL_DB_URL

def prepare_testing_data(db):
    pass

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = LOCAL_DB_URL
    client = app.test_client()

    #clear db
    db.session.query(User).delete()
    db.session.commit()
    yield client

    #after all clear db
    db.session.query(User).delete()
    db.session.commit()

def test_empty_db(client):
    """Start with a blank database."""
    response = client.get('/users')
    assert [] == response.get_json()

## USER TESTS
def test_add_user(client):
    response = client.post('/users', data=dict(username="slawek", password="test123", email="slawek@gmail.com"))
    assert 200 == response.status_code

def test_add_existing_user(client):
    pass

def test_add_existing_email_user(client):
    pass

def test_modify_user(client):
    pass

def test_get_user(client):
    pass

def test_get_register_date(client):
    pass

##
def test_upload_user_profile_photo(client):
    pass

def test_get_user_profile_photo(client):
    pass
