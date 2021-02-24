import pytest
from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from pages.my_account_page import MyAccountPage
from read_excel import ExcelReader


@pytest.mark.usefixtures("setup")
class TestLogIn:

    def test_01_blank_form(self):
        main_page = MainPage(self.driver)
        main_page.go_to_sign_in_form_from_main_page()
        sign_in_page = SignInPage(self.driver)
        sign_in_page.submit_blank_email_and_password()
        assert "Email is required." == sign_in_page.get_error_text_blank_email()
        assert "Password is required." == sign_in_page.get_error_text_blank_password()

    @pytest.mark.parametrize("data", ExcelReader.get_data_for_test_02())
    def test_02_valid_email_and_password_logged_in_and_logged_out(self, data):
        main_page = MainPage(self.driver)
        main_page.go_to_sign_in_form_from_main_page()
        sign_in_page = SignInPage(self.driver)
        sign_in_page.enter_email_and_password_and_submit(data.email, data.password)
        my_account_page = MyAccountPage(self.driver)
        my_account_page.sign_out()
        assert self.driver.current_url == "https://www.odeon.co.uk/"

    @pytest.mark.parametrize("data", ExcelReader.get_data_for_test_03())
    def test_03_invalid_email_or_password(self, data):
        main_page = MainPage(self.driver)
        main_page.go_to_sign_in_form_from_main_page()
        sing_in_page = SignInPage(self.driver)
        sing_in_page.enter_email_and_password_and_submit(data.email, data.password)
        assert "The credentials you entered are incorrect." == sing_in_page.get_error_text()

    @pytest.mark.parametrize("data", ExcelReader.get_data_for_test_04())
    def test_04_valid_email_and_blank_password(self, data):
        main_page = MainPage(self.driver)
        main_page.go_to_sign_in_form_from_main_page()
        sign_in_page = SignInPage(self.driver)
        sign_in_page.enter_email_and_password_and_submit(data.email, data.password)
        assert "Password is required." == sign_in_page.get_error_text_blank_password()

    @pytest.mark.parametrize("data", ExcelReader.get_data_for_test_05())
    def test_05_blank_email_and_valid_password(self, data):
        main_page = MainPage(self.driver)
        main_page.go_to_sign_in_form_from_main_page()
        sign_in_page = SignInPage(self.driver)
        sign_in_page.enter_email_and_password_and_submit(data.email, data.password)
        assert "Email is required." == sign_in_page.get_error_text_blank_email()