from page import BasePage
from page_locators.entity_page_locators import EntityPageLocators

class DevicesPage(BasePage):

    def goto_create_device(self):
        element = self.locate_element_by(EntityPageLocators.CREATE_ENTITY_BUTTON)
        return self.click_element(element)
    