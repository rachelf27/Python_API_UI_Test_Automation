import pytest
import pip._vendor.requests as req

def test_update_user_is_updated():
    url = 'https://reqres.in/api/users/2'
    data = {'name': 'Regina','job': "Miller's Daughter"}

    response = req.put(url, data)

    print(response.headers)

    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"