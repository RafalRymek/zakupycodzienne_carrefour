import unittest

from selenium import webdriver
from carrefourtest.pages.main_page import MainPage
from carrefourtest.pages.login_page import LoginPage
from carrefourtest.pages.delivery_date_page import DeliveryDatePage
from carrefourtest.settings import ZAKUPYCODZIENNE_URL
from webdriver_manager.chrome import ChromeDriverManager


class PurchaseSomething(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
        self.main_page = MainPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.delivery_date_page = DeliveryDatePage(self.driver)
        self.driver.maximize_window()
        self.driver.get(ZAKUPYCODZIENNE_URL)

    def test_purchase(self):
        self.main_page.agreement_confirmation()
        self.main_page.navigate_to_login_page()
        self.login_page.login()
        self.delivery_date_page.delivery_to_home()
        self.delivery_date_page.booking_the_delivery_date()
        self.main_page.add_products_to_basket()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
