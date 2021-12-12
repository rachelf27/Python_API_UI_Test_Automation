import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_1():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('http://automationpractice.com/index.php')
    chrome_driver.maximize_window()
    title = "My Store"
    assert title == chrome_driver.title
    sleep(2)
    chrome_driver.close()