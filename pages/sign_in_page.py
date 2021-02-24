from selenium.webdriver.common.by import By
import time


class SignInPage:

    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, "v-sign-in-form-field__identifier-input")
        self.password_input = (By.ID, "v-sign-in-form-field__password-input")
        self.show_password_button = (By.XPATH, "//button[@class='v-password-input__visibility-button']")
        self.sign_in_button = (By.XPATH, "//button[@type='submit']")
        self.error_text = (By.XPATH, "//div[@class='v-help-text v-help-text--style-error']")
        self.blank_email_error_text = (By.ID, "v-sign-in-form-field__identifier-input_help-text")
        self.blank_password_error_text = (By.ID, "v-sign-in-form-field__password-input_help-text")

    def submit_blank_email_and_password(self):
        self.driver.find_element(*self.sign_in_button).click()
        time.sleep(2)

    def get_error_text_blank_email(self):
        return self.driver.find_element(*self.blank_email_error_text).text

    def get_error_text_blank_password(self):
        return self.driver.find_element(*self.blank_password_error_text).text

    def enter_email_and_password_and_submit(self, email, password):
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.show_password_button).click()
        time.sleep(2)
        self.driver.find_element(*self.sign_in_button).click()
        time.sleep(2)

    def get_error_text(self):
        return self.driver.find_element(*self.error_text).text