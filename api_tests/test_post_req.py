import pytest
import pip._vendor.requests as req
import json

def test_add_user_is_created():
    url = "https://reqres.in/api/users"
    data = {'firstName': 'Faith', 'lastName': 'Moore'}

    response = req.post(url, data)

    print(response.headers)
    pretty_json = json.loads(response.text)
    print(json.dumps(pretty_json, indent=2))

    assert response.status_code == 201
    assert response.reason == "Created"
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

def test_add_user_bad_req():
    url = "https://reqres.in/api/login"
    data = {'email': 'jumob&blah'}

    response = req.post(url, data)

    print(response.headers)

    assert response.status_code == 400
    assert response.reason == "Bad Request"
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"