from ast import Lambda
from unicodedata import name
from selenium.webdriver.support.ui import WebDriverWait
from locator import *


class BasePageElement(object):
    locator = MainPageLocators.CONTAINER

    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(Lambda driver: driver.find_element(*self.locator))
