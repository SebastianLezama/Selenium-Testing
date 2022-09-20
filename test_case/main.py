import unittest
from selenium import webdriver
import page
from env import URL, USER, PASS

PATH = "C:\\Program Files (x86)\\chromedriver.exe"


class NotiCampSimple(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(PATH)
        self.driver.get(URL)
        self.driver.maximize_window()

    def test_login(self):
        login_page = page.LoginPage(self.driver)
        assert login_page.is_title_matches()
        login_page.email_element = USER
        login_page.pass_element = PASS
        login_page.click_login_button()

        main_page = page.DashBoard(self.driver)
        assert main_page.is_in_dashboard()

    # def tearDown(self) -> None:
    #     self.driver.close()


if __name__ == '__main__':
    unittest.main()
