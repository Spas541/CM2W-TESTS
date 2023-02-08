from page import BasePage
from page_elements.facilities.facility.create_facility_page_elements import FacilityNameInputElement,OrganizationNameInputElement
from page_locators.entity_page_locators import EntityPageLocators
from page_locators.facilities.facility.create_facility_page_locators import CreateFacilityPageLocators

class CreateFacilityPage(BasePage):
    facility_name = FacilityNameInputElement()
    organization_in = OrganizationNameInputElement()
    
    def select_test_organization(self):
        wraper_element = self.driver.find_element(*CreateFacilityPageLocators.ORGANIZATION_IN_WRAPER)
        wraper_element.click()
        self.organization_in = 'SPAS_TEST_ORGANIZATION'
        element = self.locate_element_by(CreateFacilityPageLocators.ORGANIZATION_ENTITY)
        self.click_element(element)

    def save_facility(self):
        element = self.driver.find_element(*EntityPageLocators.SAVE_ENTITY_BUTTON)
        element.click()

    def facility_is_saved(self):
        return self.locate_element_by(CreateFacilityPageLocators.FACILITY_IS_SAVED_LOCATOR)
       