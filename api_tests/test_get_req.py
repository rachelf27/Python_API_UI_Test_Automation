import pytest
# import requests => this is somehow showing an error "import "requests" could not be resolved from source Pylance". 
# Uninstalling and installing does not fix. See the alternate fix below
import pip._vendor.requests as req
import json

url = "https://reqres.in/api/"

def test_get_all_users():
    response = req.get(url + "users?page=2")
    print(response.headers)
    #print(response.status_code)
    #print(response.reason)
    pretty_json = json.loads(response.text)
    print(json.dumps(pretty_json, indent=2))
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
