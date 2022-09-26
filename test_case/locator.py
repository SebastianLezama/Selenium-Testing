from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    E_MAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.TAG_NAME, "button")


class MainPageLocators(object):
    CONTAINER = (By.CLASS_NAME, "mb-4")
    CAMPAIGN = (By.PARTIAL_LINK_TEXT, "Campañas")
