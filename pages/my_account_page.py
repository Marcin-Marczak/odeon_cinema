from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.sign_out_button = (By.XPATH, "//a[@class='sub--menu_link sign-out-link']")

    def sign_out(self):
        self.driver.find_element(*self.sign_out_button).click()
        WebDriverWait(self.driver, 10).until(ec.url_changes)