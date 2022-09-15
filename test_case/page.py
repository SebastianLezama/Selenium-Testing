from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import env
from locator import *


class BasePage(object):
    def __init__(self, driver) -> None:
        self.driver = driver


class LoginPage(BasePage):
    def is_title_matches(self):
        return "Notimation" in self.driver.title

    def log_in(self):
        login_email = self.driver.find_element(*LoginPageLocators.E_MAIL)
        login_email.clear()
        login_email.send_keys(env.USER)

        login_pass = self.driver.find_element(*LoginPageLocators.PASSWORD)
        login_pass.clear()
        login_pass.send_keys(env.PASS)
        login_pass.send_keys(Keys.RETURN)


class DashBoard(BasePage):
    def is_in_dashboard(self):
        main_container = self.driver.find_element(*MainPageLocators.CONTAINER)
        return "col py-3 px-5" in main_container
