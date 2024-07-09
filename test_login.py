import pytest

EMAIL_FIELD = ("xpath", "//input[@id='email']")
PASSWORD_FIELD = ("xpath",  "//input[@id='pass']")
SING_IN_BUTTON = ("xpath", "//button[@id='send2']")
MESSAGE_ERROR_FIELD = (
    "xpath", "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']")

users = ["test1@magento.com", "test2@magento.com", "test3@magento.com"]
password = ["pass123", "pass345", "pass678"]


def generate_pairs():
    pairs = []
    for user in users:
        for passw in password:
            pairs.append(pytest.param((user, passw), id=f"{user}, {passw}"))
    return pairs

# @pytest.mark.parametrize(
#     "creds",
#     [
#         pytest.param(("test1@magento.com", "pass123"),
#                      id="test1@magento.com, pass123"),
#         pytest.param(("test2@magento.com", "pass345"),
#                      id="test2@magento.com, pass345"),
#         pytest.param(("test3@magento.com", "pass678"),
#                      id="test3@magento.com, pass678"),
#     ]
# )


@pytest.mark.regression
@pytest.mark.parametrize("creds", generate_pairs())
def test_login(driver, creds):
    login, password = creds
    driver.implicitly_wait(5)
    driver.get("https://magento.softwaretestingboard.com/customer/account/login/")
    driver.find_element(
        *EMAIL_FIELD).send_keys(login)
    driver.find_element(*PASSWORD_FIELD).send_keys(password)
    driver.find_element(*SING_IN_BUTTON).click()
    message_error = driver.find_element(*MESSAGE_ERROR_FIELD).text
    assert message_error == "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."
