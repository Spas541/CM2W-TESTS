from selenium.webdriver.support.select import Select
from page import BasePage
from page_elements.users.user.create_user_page_elements import UserConfirmPasswordInputElement,UserEmailInputElement,UserEmployeeInInputElement,UserFirstNameInputElement,UserLastNameInputElement,UserPasswordInputElement
from page_locators.users.user.create_user_page_locators import CreateUserPageLocators
from page_locators.entity_page_locators import EntityPageLocators

class CreateUserPage(BasePage):
    user_first_name = UserFirstNameInputElement()
    user_last_name = UserLastNameInputElement()
    user_email = UserEmailInputElement()
    employee_in = UserEmployeeInInputElement()
    user_password = UserPasswordInputElement()
    user_confirm_password = UserConfirmPasswordInputElement()
    

    def goto_password_tab(self):
        element = self.driver.find_element(*CreateUserPageLocators.PASSWORD_TAB)
        element.click()

    def select_user_role(self):
        sel = Select(self.driver.find_element(*CreateUserPageLocators.USER_ROLE_SELECT))
        sel.select_by_visible_text("Super User")

    def select_employee_in_organization(self):
        wraper_element = self.driver.find_element(*CreateUserPageLocators.EMPLOYEE_IN_WRAPER)
        wraper_element.click()
        self.employee_in = 'SPAS_TEST_ORGANIZATION'
        element = self.locate_element_by(CreateUserPageLocators.EMPLOYEE_IN_ORGANIZATION_ENTITY)
        self.click_element(element)
        
    def save_user(self):
        element = self.driver.find_element(*EntityPageLocators.SAVE_ENTITY_BUTTON)
        element.click()
    
    def user_is_saved(self):
        return self.locate_element_by(CreateUserPageLocators.USER_IS_SAVED)