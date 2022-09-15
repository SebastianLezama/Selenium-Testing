from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    E_MAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")


class MainPageLocators(object):
    CONTAINER = (By.CLASS_NAME, "col py-3 px-5")
