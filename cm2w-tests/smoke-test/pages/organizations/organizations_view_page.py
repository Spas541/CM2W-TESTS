from page import BasePage
from page_elements.organizations.organizations_view_elements import OrganizationSearchNameInputElement
from page_locators.entity_page_locators import EntityPageLocators
from page_locators.organizations.organizations_view_locators import OrganizationsViewLocators
from page_locators.organizations.organization.view_organization_page_locators import ViewOrganizationPageLocators

class OrganizationsPage(BasePage):
    search_org_name = OrganizationSearchNameInputElement()

    def search_test_organization(self):
        self.search_org_name = 'SPAS_TEST_ORGANIZATION'
        return self.locate_element_by(OrganizationsViewLocators.SEARCH_TEST_ORG_RESULT)

    def goto_test_org_view(self):
        element = self.locate_element_by(OrganizationsViewLocators.SEARCH_TEST_ORG_RESULT)
        return self.click_element(element)

    def goto_create_organization(self):
        element = self.locate_element_by(EntityPageLocators.CREATE_ENTITY_BUTTON)
        return self.click_element(element)
        