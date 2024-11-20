import requests

base_url = 'https://reqres.in/api/'

payload_get = {'page': '1', 'per_rage': '2'}
payload_post = {'email': 'eve.holt@reqres.in', 'password': 'cityslicka'}


def test_get_user():
    url = base_url + 'user'
    response = requests.get(url, payload_get)
    assert response.status_code == 200


def test_login_positive():
    url = base_url + 'login'
    response = requests.post(url, data=payload_post)
    assert response.status_code == 200


def test_login_negative():
    url = base_url + 'login'
    response = requests.post(url)
    assert response.status_code == 400


def test_update_user():
    url = base_url + 'users/{id}'
    response = requests.put(url)
    assert response.status_code == 200


def test_for_404():
    response = requests.post(url='https://reqres.in/apii/')
    assert response.status_code == 404


def test_delete_resource():
    url = base_url + '{resource}/{id}'
    response = requests.delete(url)
    assert response.status_code == 204
