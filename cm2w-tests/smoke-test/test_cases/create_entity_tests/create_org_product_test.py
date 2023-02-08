import unittest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.login_page import LoginPage 
from pages.home_page import HomePage
from pages.organizations.organizations_view_page import OrganizationsPage
from pages.organizations.organization.view_organization_page import ViewOrganizationPage


class CreateOrgProductTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:4200")
        login_page = LoginPage(self.driver)
        login_page.email_input_element = 'stuhlov@cm2w.net'
        login_page.password_input_element = '@Stuhlov1234'
        
        login_page.click_login_button()
  
    def test_create_org_product(self):
        home_page = HomePage(self.driver)
        self.driver.maximize_window()
        self.assertTrue(home_page.is_loged_in(), 'Unsuccessfull LOGIN')
        self.assertTrue(home_page.goto_organizations(), 'Unsuccessfull routing to ORGANIZATIONS page')
        organizations_page = OrganizationsPage(self.driver)
        self.assertTrue(organizations_page.search_test_organization(),'Test organization not found')
        organizations_page.goto_test_org_view()
        test_org_page = ViewOrganizationPage(self.driver)
        test_org_page.go_to_org_prod_tab()
        test_org_page.create_org_prod()
        test_org_page.new_prod_name = 'TEST_PROD'
        test_org_page.new_prod_price = 2.99
        test_org_page.save_prod()
        self.assertTrue(test_org_page.prod_is_saved(), 'Test PRODUCT is not saved')

    def test_import_org_product(self):
        home_page = HomePage(self.driver)
        self.driver.maximize_window()
        self.assertTrue(home_page.is_loged_in(), 'Unsuccessfull LOGIN')
        self.assertTrue(home_page.goto_organizations(), 'Unsuccessfull routing to ORGANIZATIONS page')
        organizations_page = OrganizationsPage(self.driver)
        self.assertTrue(organizations_page.search_test_organization(),'Test organization not found')
        organizations_page.goto_test_org_view()
        test_org_page = ViewOrganizationPage(self.driver)
        test_org_page.go_to_org_prod_tab()
        test_org_page.open_products_options()
        test_org_page.show_import_org_prod_modal()
        org_prods_count = len(test_org_page.org_prods_list())
        time.sleep(3)
        test_org_page.import_org_prod()
        time.sleep(3)
        self.assertNotEqual(org_prods_count, len(test_org_page.org_prods_list()), "Prod isnt imported")
        #self.assertTrue(test_org_page.prod_is_imported(), 'Unsuccessfull importing org product from parent org')

       

          

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()