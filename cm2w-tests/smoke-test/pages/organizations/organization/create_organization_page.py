from selenium.webdriver.support.select import Select
from page import BasePage
from page_elements.organizations.organization.create_organization_page_elements import OrganizationNameInputElement
from page_locators.organizations.organization.create_organization_page_locators import CreateOrganizationPageLocators
from page_locators.entity_page_locators import EntityPageLocators



class CreateOrganizationPage(BasePage):
    organization_name = OrganizationNameInputElement()

    def goto_preferences_tab(self):
        element = self.driver.find_element(*CreateOrganizationPageLocators.PREFERENCES_TAB)
        element.click()

    def select_organization_domain(self):
        sel = Select(self.driver.find_element(*CreateOrganizationPageLocators.ORGANIZATION_DOMAIN_SELECT))
        sel.select_by_visible_text("CM2W")

    def select_organization_currency(self):
        sel = Select(self.driver.find_element(*CreateOrganizationPageLocators.ORGANIZATION_CURRENCY_SELECT))
        sel.select_by_index(6)

        
    def save_organization(self):
        element = self.driver.find_element(*EntityPageLocators.SAVE_ENTITY_BUTTON)
        element.click()
        

    def org_is_saved(self):
        return self.locate_element_by(CreateOrganizationPageLocators.ORGANIZATION_IS_SAVED_LOCATOR)

    def sub_org_is_saved(self):
        return self.locate_element_by(CreateOrganizationPageLocators.SUB_ORGANIZATION_IS_SAVED_LOCATOR)
        
        