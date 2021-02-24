from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.cookie = (By.ID, "onetrust-accept-btn-handler")
        self.sign_in_button = (By.LINK_TEXT, "Sign in")

    def go_to_sign_in_form_from_main_page(self):
        self.driver.get("https://www.odeon.co.uk/")
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable, self.driver.find_element(*self.cookie))
        self.driver.find_element(*self.cookie).click()
        self.driver.find_element(*self.sign_in_button).click()
        WebDriverWait(self.driver, 10).until(ec.url_changes)