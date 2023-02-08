import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.login_page import LoginPage 
from pages.home_page import HomePage
from pages.organizations.organizations_view_page import OrganizationsPage
from pages.organizations.organization.view_organization_page import ViewOrganizationPage
from pages.organizations.organization.create_organization_page import CreateOrganizationPage


class CreateOrgTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:4200")
        login_page = LoginPage(self.driver)
        login_page.email_input_element = 'stuhlov@cm2w.net'
        login_page.password_input_element = '@Stuhlov1234'
        
        login_page.click_login_button()
        
    def test_1create_organization(self):
        home_page = HomePage(self.driver)
        self.assertTrue(home_page.is_loged_in(), 'Unsuccessfull LOGIN')
        self.assertTrue(home_page.goto_organizations(), 'Unsuccessfull routing to ORGANIZATIONS page')
        organizations_page = OrganizationsPage(self.driver)
        self.assertTrue(organizations_page.goto_create_organization(), 'Unsuccessfull routing to create ORGANIZATIONS page')
        create_organization_page = CreateOrganizationPage(self.driver)
        create_organization_page.organization_name = 'SPAS_TEST_ORGANIZATION'
        create_organization_page.select_organization_domain()
        create_organization_page.goto_preferences_tab()
        create_organization_page.select_organization_currency()
        create_organization_page.save_organization()
        self.assertTrue(create_organization_page.org_is_saved(), 'Error when saving the test ORGANIZATION')

    def test_2create_sub_organization(self):
        home_page = HomePage(self.driver)
        self.assertTrue(home_page.is_loged_in(), 'Unsuccessfull LOGIN')
        self.assertTrue(home_page.goto_organizations(), 'Unsuccessfull routing to ORGANIZATIONS page')
        organizations_page = OrganizationsPage(self.driver)
        self.assertTrue(organizations_page.search_test_organization(),'Test organization not found')
        organizations_page.goto_test_org_view()
        test_org_page = ViewOrganizationPage(self.driver)
        test_org_page.add_sub_org()
        create_organization_page = CreateOrganizationPage(self.driver)
        create_organization_page.organization_name = 'SPAS_TEST_SUB_ORGANIZATION'
        create_organization_page.select_organization_domain()
        create_organization_page.goto_preferences_tab()
        create_organization_page.select_organization_currency()
        create_organization_page.save_organization()
        self.assertTrue(create_organization_page.sub_org_is_saved(), 'Error when saving the test SUB_ORGANIZATION')

        
      

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()