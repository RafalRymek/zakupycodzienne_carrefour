from carrefourtest.locators. login_selectors import *
from carrefourtest.settings import *


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.find_element(*username).send_keys(USER_LOGIN)
        self.driver.find_element(*password).send_keys(USER_PASSWORD)
        self.driver.find_element(*submit_button).click()
