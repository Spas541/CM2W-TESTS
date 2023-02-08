from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    """A class for login page locators. All main page locators should come here"""

    LOGIN_BUTTON = (By.XPATH, "//button[@type='button']")