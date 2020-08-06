from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from carrefourtest.locators.main_selectors import *
from carrefourtest.locators.login_selectors import *
from carrefourtest.settings import shopping_list
from selenium.webdriver.common.keys import Keys


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def agreement_confirmation(self):
        agreement_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Wyrażam')]")))
        agreement_button.click()

    def navigate_to_login_page(self):
        self.driver.find_element(*login_button).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(username))

    def delivery_date_booking(self):
        self.driver.find_element_by_xpath(chosen_date).click()

    def search_for_product(self, product):
        self.driver.find_element(*search_field_selector).send_keys(product)
        self.driver.find_element(*magnifier_search).click()

    def add_product_to_basket(self):
        try:
            add_basket_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Do koszyka')]")))
            add_basket_button.click()
        except TimeoutException as e:
            print("Element not found. Error: {}".format(str(e)))

    # clear method for windows
    # def clear_input_search_for_win(self):
    #     self.driver.find_element(*search_field_selector).send_keys(Keys.CONTROL, "a" + Keys.BACKSPACE)

    def clear_input_search_for_mac(self):
        element = self.driver.find_element_by_xpath("//input[@id='search-input']")
        search = len(element.get_attribute('value'))
        element.send_keys(search * Keys.BACKSPACE)

    def add_products_to_basket(self):
        for product in shopping_list:
            self.search_for_product(product)
            self.add_product_to_basket()
            self.clear_input_search_for_mac()
