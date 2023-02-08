from page import BasePage
from page_locators.facilities.facility.view_facility_page_locators import ViewFacilityPageLocators
from page_elements.facilities.facility.view_facility_page_elements import SearchUserInputElement, FilterUserInputElement

class ViewFacilityPage(BasePage):

    search_input_element = SearchUserInputElement()
    filter_user_input_element = FilterUserInputElement()

    def go_to_fac_prod_tab(self):
        element = self.locate_element_by(ViewFacilityPageLocators.FAC_PROD_TAB)
        return self.click_element(element)

    def go_to_users_tab(self):
        element = self.locate_element_by(ViewFacilityPageLocators.USERS_TAB)
        return self.click_element(element)
    
    def show_grant_user_access_popup(self):
        options_element = self.locate_element_by(ViewFacilityPageLocators.OPTIONS_BUTTON)
        self.click_element(options_element)
        element = self.locate_element_by(ViewFacilityPageLocators.GRANT_FAC_ACCESS_BUTTON)
        return self.click_element(element)

    def show_user_filter(self):
        element = self.locate_element_by(ViewFacilityPageLocators.SHOW_USER_FILTER)
        return self.click_element(element)

    def grant_testuser_facility_access(self):
        try:
            self.locate_element_by(ViewFacilityPageLocators.TEST_USER_ELEMENT)
        finally:
            try:
                grant_access_element = self.locate_element_by(ViewFacilityPageLocators.GRANT_ACCESS_SWITCH)
            finally:
                return self.click_element(grant_access_element)

    def close_popup(self):
        element = self.locate_element_by(ViewFacilityPageLocators.CLOSE_GRANT_ACCESS_POPUP)
        return self.click_element(element)
        
    def user_access_is_granted(self):
        return self.locate_element_by(ViewFacilityPageLocators.TEST_USER_LOCATED)

    def show_import_org_prod_popup(self):
        element = self.locate_element_by(ViewFacilityPageLocators.SHOW_IMPORT_PROD_POPUP)
        return self.click_element(element)

    def import_org_prod(self):
        element = self.locate_element_by(ViewFacilityPageLocators.IMPORT_PROD_BUTTON)
        return self.click_element(element)

    def prod_is_saved(self):
        return self.locate_element_by(ViewFacilityPageLocators.PRODS_ARE_SAVED)

    

    
        
 
 
