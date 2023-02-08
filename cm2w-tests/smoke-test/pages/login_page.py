from page import BasePage
from page_elements.login_page_elements import EmailInputElement,PasswordInputElement
from page_locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    email_input_element = EmailInputElement()
    password_input_element = PasswordInputElement()

    def click_login_button(self):
        element = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        element.click()