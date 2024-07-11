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
        logins.get_message_error()
