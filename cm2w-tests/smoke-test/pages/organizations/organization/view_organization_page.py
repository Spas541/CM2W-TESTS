from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from page import BasePage
from page_elements.organizations.organization.view_organization_page_elements import NewOrgProdNameInput,NewOrgProdPriceInput,NewNotTemplateName,OrgProdsContainer
from page_locators.organizations.organization.view_organization_page_locators import ViewOrganizationPageLocators

class ViewOrganizationPage(BasePage):
    new_prod_name = NewOrgProdNameInput()
    new_prod_price = NewOrgProdPriceInput()
    new_not_template_name = NewNotTemplateName()
    org_prods_container = OrgProdsContainer()

    def go_to_org_prod_tab(self):
        element = self.locate_element_by(ViewOrganizationPageLocators.ORG_PROD_TAB)
        return self.click_element(element)

    def create_org_prod(self):
        element = self.locate_element_by(ViewOrganizationPageLocators.ADD_PROD_BUTTON)
        return self.click_element(element)

    def add_sub_org(self):
        element = self.locate_element_by(ViewOrganizationPageLocators.ADD_SUB_ORG_BUTTON)
        return self.click_element(element)

    def go_to_not_template_tab(self):
        element = self.locate_element_by(ViewOrganizationPageLocators.NOT_TEMPLATE_TAB)
        return self.click_element(element)
    
    def select_not_template_lvl(self):
        sel = Select(self.driver.find_element(*ViewOrganizationPageLocators.NOT_TEMPLATE_LVL_SELECT))
        sel.select_by_index(1)

    def create_not_template(self):
        element = self.locate_element_by(ViewOrganizationPageLocators.ADD_NOT_TEMPLATE_BUTTON)
        return self.click_element(element)

    def open_products_options(self):
        element = self.locate_element_by(ViewOrganizationPageLocators.OPTIONS_BUTTON)
        return self.click_element(element)

    def show_import_org_prod_modal(self):
        element = self.locate_element_by(ViewOrganizationPageLocators.SHOW_IMPORT_ORG_PRODUCT_MODAL_BUTTON)
        return self.click_element(element)

    def import_org_prod(self):
        element = self.locate_element_by(ViewOrganizationPageLocators.IMPORT_PROD_BUTTON)
        return self.click_element(element)

    def prod_is_imported(self):
        return self.locate_element_by(ViewOrganizationPageLocators.PROD_IS_IMPORTED)

    def org_prods_list(self):
        return self.org_prods_container.find_elements(By.CLASS_NAME, "list-item")

    def save_prod(self):
        element = self.locate_element_by(ViewOrganizationPageLocators.SAVE_PROD_BUTTON)
        return self.click_element(element)

    def prod_is_saved(self):
        return self.locate_element_by(ViewOrganizationPageLocators.PROD_IS_SAVED)
    
    def save_not_template(self):
        element = self.locate_element_by(ViewOrganizationPageLocators.SAVE_TEMPLATE_BUTTON)
        return self.click_element(element)

    def not_template_is_saved(self):
        return self.locate_element_by(ViewOrganizationPageLocators.NOT_TEMPLATE_IS_SAVED)

    

    
        
 
 
