import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import page
import env

PATH = "C:\\Program Files (x86)\\chromedriver.exe"


class NotiCampSimple(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(PATH)
        self.driver.get(env.URL)

    def test_title(self):
        loginPage = page.LoginPage()
        assert loginPage.is_title_matches()

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
