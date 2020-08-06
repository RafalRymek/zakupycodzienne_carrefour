from selenium.webdriver.common.by import By

chosen_date = (By.XPATH, "//span[contains(text(),'Dostawa do domu') or contains(text(),'rozpocznij zakupy')]")
purchase_start_button = (By.XPATH, "//span[contains(text(),'rozpocznij zakupy')]")
delivery_to_home = (By.XPATH, "//input[@name='zipCode']/ancestor::label")
available_dates = (By.XPATH, "//p[contains(.,'Dostępne')]/following-sibling::div//input/..  ")
clear_choose_city = (By.XPATH, "//button[@title='wyczyść']")
choose_city = (By.XPATH, "//li[@class='MuiAutocomplete-option' and contains(text(),'Kraków')]")
city_picker = (By.XPATH,
               "//input[@class='MuiInputBase-input MuiInput-input MuiAutocomplete-input MuiAutocomplete-inputFocused "
               "MuiInputBase-inputAdornedEnd']")


