import os
import tempfile
import pytest
import json
from app import app, db
from model.user import User
from config import LOCAL_DB_URL

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = LOCAL_DB_URL
    client = app.test_client()

    #clear db before test
    db.session.query(User).delete()
    db.session.commit()
    yield client

    #cleaer db after test
    db.session.query(User).delete()
    db.session.commit()

## USER POST TESTS
def test_add_user(client):
    response = client.post('/users', data=dict(username="slawek", password="test123", email="slawek@gmail.com"))
    assert 200 == response.status_code

def test_add_existing_user(client):
    response = client.post('/users', data=dict(username="username1", password="aaabbb", email="aaa@gmail.com"))
    response = client.post('/users', data=dict(username="username1", password="qqqbbb", email="qqq@gmail.com"))
    assert 409 == response.status_code


def test_add_existing_email_user(client):
    response = client.post('/users', data=dict(username="usernameX", password="qqqbbb", email="qqq@gmail.com"))
    response = client.post('/users', data=dict(username="usernameY", password="qqqbbb", email="qqq@gmail.com"))
    assert 409 == response.status_code

def test_email_field_is_missing(client):
    response = client.post('/users', data=dict(username="test123", password="test123"))
    assert 400 == response.status_code
def test_email_is_not_valid(client):
    response = client.post('/users', data=dict(username="test123", password="test123", email="wrong"))
    assert 422 == response.status_code

## USER PUT TESTS
def test_modify_user_email(client):
    client.post('/users', data=dict(username="username1", password="aaabbb", email="aaa@gmail.com"))
    response = client.put('/users/username1', data=dict(email="new_username_email@gmail.com"))
    assert 200 == response.status_code
    user = client.get('/users/username1')
    assert "new_username_email@gmail.com" == user.get_json()['email']

def test_modify_user_password_with_wrong_password(client):
    client.post('/users', data=dict(username="username2", password="test123", email="aaa@gmail.com"))
    response = client.put('/users/username2', data=dict(old_password="wrong_password", new_password="xxxxxxx"))
    assert 400 == response.status_code

def test_modify_user_password(client):
    client.post('/users', data=dict(username="username2", password="password2", email="aaa@gmail.com"))
    response = client.put('/users/username2', data=dict(old_password="password2", new_password="xxxxxxx"))
    assert 200 == response.status_code

## USER GET TESTS
def test_get_user(client):
    client.post('/users', data=dict(username="username3", password="password3", email="username3@gmail.com"))
    user = client.get('/users/username3').get_json()

    assert "username3" == user["username"]
    assert "username3@gmail.com" == user["email"]
    assert "register_date" in user

'''
def test_get_register_date(client):
    pass

##
def test_upload_user_profile_photo(client):
    pass

def test_get_user_profile_photo(client):
    pass
'''