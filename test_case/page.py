from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import env
import locator as LC
from element import BasePageElement


class LoginUserInput(BasePageElement):
    locator = LC.LoginPageLocators.E_MAIL


class LoginPasswordInput(BasePageElement):
    locator = LC.LoginPageLocators.PASSWORD


class MainContainer(BasePageElement):
    locator = LC.MainPageLocators.CONTAINER


class BasePage(object):
    def __init__(self, driver) -> None:
        self.driver = driver


class LoginPage(BasePage):
    email_element = LoginUserInput()
    pass_element = LoginPasswordInput()

    def is_title_matches(self):
        return "Notimation" in self.driver.title

    def click_login_button(self):
        element = self.driver.find_element(*LC.LoginPageLocators.LOGIN_BUTTON)
        element.click()


class DashBoard(BasePage):
    container_element = MainContainer()

    def is_in_dashboard(self):
        self.driver.implicitly_wait(5)
        main_container = self.driver.find_element(
            *LC.MainPageLocators.CONTAINER)
        return "mb-4" in main_container
