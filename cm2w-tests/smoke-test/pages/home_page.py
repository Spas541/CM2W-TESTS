from page import BasePage
from page_locators.home_page_locators import HomePageLocators

class HomePage(BasePage):
    
    def is_loged_in(self):
        return self.locate_element_by(HomePageLocators.USER_ICON)
        
    def goto_organizations(self):
        element = self.locate_element_by(HomePageLocators.ORGANIZATIONS_MENU_BUTTON)
        return self.click_element(element)

    def goto_users(self):
        element = self.locate_element_by(HomePageLocators.USERS_MENU_BUTTON)
        return self.click_element(element)

    def goto_facilities(self):
        element = self.locate_element_by(HomePageLocators.FACILITIES_MENU_BUTTON)
        return self.click_element(element)

    def goto_devices(self):
        element = self.locate_element_by(HomePageLocators.DEVICES_MENU_BUTTON)
        return self.click_element(element)