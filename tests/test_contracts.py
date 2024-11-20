import json
import os

import requests
from jsonschema import validate

from files.schema import validate_users


def test_schema_validate_user():
    response = requests.get('https://reqres.in/api/users?page=1&per_page=2')
    body = response.json()
    assert response.status_code == 200
    validate(instance=body, schema=validate_users)


def test_schema_validate_first_name_and_email():
    first_name = 'George'
    email = 'george.bluth@reqres.in'

    response = requests.post('https://reqres.in/api/users?page=1&per_page=2',
                             data={f'first_name': first_name, 'email': email})
    body = response.json()
    assert response.status_code == 201
    assert body['first_name'] == first_name
    assert body['email'] == email


def test_schema_validate_file():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    path_json = os.path.join(project_root, 'files', 'validate_file.json')
    response = requests.post('https://reqres.in/api/users?page=1&per_page=2',
                             data={'first_name': 'George', 'email': 'george.bluth@reqres.in'})
    body = response.json()
    with open(path_json) as file:
        validate(instance=body, schema=json.load(file))


def test_get_users():
    response = requests.get(
        url="https://reqres.in/api/users",
        params={"page": 1, "per_page": 2},
        verify=False
    )
    ids = [element["first_name"] for element in response.json()["data"]]

    assert len(ids) == len(set(ids))
    assert response.status_code == 200
