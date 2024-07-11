class LoginPageLocators:
    EMAIL_FIELD = ("xpath", "//input[@id='email']")
    PASSWORD_FIELD = ("xpath",  "//input[@id='pass']")
    SING_IN_BUTTON = ("xpath", "//button[@id='send2']")
    MESSAGE_ERROR_FIELD = (
        "xpath", "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']")
