import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.login_page import LoginPage 
from pages.home_page import HomePage
from pages.organizations.organizations_view_page import OrganizationsPage
from pages.organizations.organization.view_organization_page import ViewOrganizationPage


class CreateNotTemplateTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:4200")
        login_page = LoginPage(self.driver)
        login_page.email_input_element = 'stuhlov@cm2w.net'
        login_page.password_input_element = '@Stuhlov1234'
        
        login_page.click_login_button()
  
    def test_create_not_template(self):
        home_page = HomePage(self.driver)
        self.assertTrue(home_page.is_loged_in(), 'Unsuccessfull LOGIN')
        self.assertTrue(home_page.goto_organizations(), 'Unsuccessfull routing to ORGANIZATIONS page')
        organizations_page = OrganizationsPage(self.driver)
        self.assertTrue(organizations_page.search_test_organization(),'Test organization not found')
        organizations_page.goto_test_org_view()
        test_org_page = ViewOrganizationPage(self.driver)
        test_org_page.go_to_not_template_tab()
        test_org_page.create_not_template()
        test_org_page.new_not_template_name = 'TEST_NOT_TEMPLATE'
        test_org_page.select_not_template_lvl()
        test_org_page.save_not_template()
        self.assertTrue(test_org_page.not_template_is_saved(), 'Test NOTIFICATION TEMPLATE is not saved')
          

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()