from page import BasePage
from page_locators.entity_page_locators import EntityPageLocators
from page_locators.facilities.facilities_view_page_locators import FacilitiesViewLocators
from page_elements.facilities.facilities_view_page_elements import FacilitySearchNameInputElement

class FacilitiesPage(BasePage):
    search_fac_name = FacilitySearchNameInputElement()

    def search_test_facility(self):
        self.search_fac_name = 'SPAS_TEST_FACILITY'
        return self.locate_element_by(FacilitiesViewLocators.SEARCH_TEST_FACILITY_RESULT)

    def goto_test_facility_view(self):
        element = self.locate_element_by(FacilitiesViewLocators.SEARCH_TEST_FACILITY_RESULT)
        return self.click_element(element)

    def goto_create_facility(self):
        element = self.locate_element_by(EntityPageLocators.CREATE_ENTITY_BUTTON)
        return self.click_element(element)
    