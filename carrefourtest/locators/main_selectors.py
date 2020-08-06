from selenium.webdriver.common.by import By

agreement_button = (By.XPATH, ".//span[contains(text(),'Wyrażam')]")
login_button = (By.XPATH, "//b[contains(text(),'Zaloguj')]")
search_field_selector = (By.XPATH, "//input[@id='search-input']")
magnifier_search = (By.XPATH, "//*[@class='MuiButton-label']/*[@class='MuiSvgIcon-root']/..")
chosen_date = (By.XPATH, "//span[contains(text(),'Dostawa do domu')]")
add_to_basket = (By.XPATH, " //span[contains(text(),'Do koszyka')]")

