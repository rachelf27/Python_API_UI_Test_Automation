import pytest
import pip._vendor.requests as req
import json

def test_malformed_xml():
    url = "<URL goes here"
    mal_xml = """<InventoryUpdate><Username>api_user@example.com"""
    content_type = 'application/xml'
    response = req.post(url, mal_xml, content_type)
    print(response.headers)

    #assert for error

def test_sql_inject():
    url = "URL goes here"
    sql = "1=1"
    response = req.post(url, sql)
    print(response.headers)
    #assert for error


def test_xpath_inject():
    url = "URL goes here"
    xpath = "/users/user[@username='"
    response = req.post(url, xpath)
    print(response.headers)
    #assert for error


def test_xss():
    url = "URL goes here"
    xss = "<script>alert(‘XSS’)</script>"
    response = req.post(url, xss)
    print(response.headers)
    #assert for error

"""
def test_invalid_types():
    response = req.get(url)

def test_boundary_scan():
    response = req.get(url)

def test_broken_auth():
    response = req.get(url)
 """
