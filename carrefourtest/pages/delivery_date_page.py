from selenium.webdriver.support.wait import WebDriverWait
from carrefourtest.locators.delivery_date_selectors import *
from selenium.webdriver.support import expected_conditions as EC


class DeliveryDatePage:

    def __init__(self, driver):
        self.driver = driver

    def delivery_to_home(self):
        self.driver.find_element(*chosen_date).click()

    def booking_the_delivery_date(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(city_picker)).click()
        self.driver.find_element(*choose_city).click()
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(delivery_to_home)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(available_dates)).click()
        self.driver.find_element(*purchase_start_button).click()
