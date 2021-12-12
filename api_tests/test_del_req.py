import pytest
import pip._vendor.requests as req

def test_delete_user():
    url = 'https://reqres.in/api/users/2'

    response = req.delete(url)

    print(response.headers)

    assert response.status_code == 204
    assert response.reason == "No Content"
