import pytest
from pages.login_page import LoginPage
from generator import generate_pairs


class TestLogin:
    @pytest.mark.parametrize("creds", generate_pairs())
    @pytest.mark.regression
    def test_login(self, driver, creds):
        link = "https://magento.softwaretestingboard.com/customer/account/login/"
        logins = LoginPage(driver, link)
        logins.open_page()
        logins.go_to_login_page(creds)
        message_error = logins.get_message_error()
        assert message_error == "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."
