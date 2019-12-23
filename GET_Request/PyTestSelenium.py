from webbrowser import Chrome
from selenium.webdriver import chrome
from selenium import webdriver
import pytest

path='C:\\chromedriver\\chromedriver.exe'

driver = Chrome(executable_path=path)

driver.get('http://www.thetestingworld.com/testings')