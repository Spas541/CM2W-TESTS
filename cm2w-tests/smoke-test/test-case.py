import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.login_page import LoginPage 
from pages.home_page import HomePage
from pages.organizations.organizations_view_page import OrganizationsPage
from pages.organizations.organization.create_organization_page import CreateOrganizationPage
from pages.organizations.organization.view_organization_page import ViewOrganizationPage
from pages.users.users_view_page import UsersPage
from pages.users.user.create_user_page import CreateUserPage
from pages.facilities.facilities_view_page import FacilitiesPage
from pages.facilities.facility.view_facility_page import ViewFacilityPage
from pages.facilities.facility.create_facility_page import CreateFacilityPage
from pages.devices.devices_view_page import DevicesPage
from pages.devices.device.create_device_page import CreateDevicePage


class Cm2WSmokeTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:4200")
        login_page = LoginPage(self.driver)
        login_page.email_input_element = 'stuhlov@cm2w.net'
        login_page.password_input_element = '@Stuhlov1234'
        
        login_page.click_login_button()
        
    def test_7create_organization(self):
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
        
    def test_2create_user(self):
        home_page = HomePage(self.driver)
        self.assertTrue(home_page.is_loged_in(), 'Unsuccessfull LOGIN')
        self.assertTrue(home_page.goto_users(), 'Unsuccessfull routing to USERS page')
        users_page = UsersPage(self.driver)
        self.assertTrue(users_page.goto_create_user(),'Unsuccessfull routing to create USER page')
        create_user_page = CreateUserPage(self.driver)
        create_user_page.user_first_name = 'SPAS_TEST'
        create_user_page.user_last_name = 'SUPER_USER'
        create_user_page.user_email = 'SPAS_TEST_SUPERUSER@ABV.BG'
        create_user_page.select_user_role()
        create_user_page.select_employee_in_organization()
        create_user_page.goto_password_tab()
        create_user_page.user_password = '@12345678'
        create_user_page.user_confirm_password = '@12345678'
        create_user_page.save_user()
        self.assertTrue(create_user_page.user_is_saved(), 'Error when saving the test USER')

    def test_3create_facility(self):
        home_page = HomePage(self.driver)
        self.assertTrue(home_page.is_loged_in(), 'Unsuccessfull LOGIN')
        self.assertTrue(home_page.goto_facilities(), 'Unsuccessfull routing to FACILITIES page')
        facilities_page = FacilitiesPage(self.driver)
        self.assertTrue(facilities_page.goto_create_facility(),'Unsuccessfull routing to create FACILITY page')
        create_facility_page = CreateFacilityPage(self.driver)
        create_facility_page.facility_name = 'SPAS_TEST_FACILITY'
        create_facility_page.save_facility()
        self.assertTrue(create_facility_page.facility_is_saved(), 'Error when saving the test FACILITY')

    def test_4create_device(self):
        home_page = HomePage(self.driver)
        self.assertTrue(home_page.is_loged_in(), 'Unsuccessfull LOGIN')
        self.assertTrue(home_page.goto_devices(), 'Unsuccessfull routing to DEVICES page')
        devices_page = DevicesPage(self.driver)
        self.assertTrue(devices_page.goto_create_device(),'Unsuccessfull routing to create DEVICE page')
        create_device_page = CreateDevicePage(self.driver)
        create_device_page.device_name = 'SPAS_TEST_DEVICE'
        create_device_page.device_sn = 'W88772'
        create_device_page.select_facility()
        create_device_page.save_device()
        self.assertTrue(create_device_page.device_is_saved(), 'Error when saving the test DEVICE')

  
    def test_5create_org_product(self):
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


    def test_6import_org_prod(self):
        home_page = HomePage(self.driver)
        self.driver.maximize_window()
        self.assertTrue(home_page.is_loged_in(), 'Unsuccessfull LOGIN')
        self.assertTrue(home_page.goto_facilities(), 'Unsuccessfull routing to FACILITIES page')
        facilities_page = FacilitiesPage(self.driver)
        self.assertTrue(facilities_page.search_test_facility(),'Test facility not found')
        facilities_page.goto_test_facility_view()
        test_facility_page = ViewFacilityPage(self.driver)
        test_facility_page.go_to_fac_prod_tab()
        test_facility_page.show_import_org_prod_popup()
        test_facility_page.import_org_prod()
        self.assertTrue(test_facility_page.prod_is_saved(), 'Failed importing org products')

    def test_1grant_user_explicit_facility_access(self):
        home_page = HomePage(self.driver)
        self.driver.maximize_window()
        self.assertTrue(home_page.is_loged_in(), 'Unsuccessfull LOGIN')
        self.assertTrue(home_page.goto_facilities(), 'Unsuccessfull routing to FACILITIES page')
        facilities_page = FacilitiesPage(self.driver)
        self.assertTrue(facilities_page.search_test_facility(), 'Test facility not found')
        facilities_page.goto_test_facility_view()
        test_facility_page = ViewFacilityPage(self.driver)
        test_facility_page.go_to_users_tab()
        test_facility_page.show_grant_user_access_popup()
        time.sleep(3)
        test_facility_page.search_input_element = 'SPAS_TEST SUPER_USER'
        time.sleep(3)
        test_facility_page.grant_testuser_facility_access()
        time.sleep(3)
        test_facility_page.close_popup()
        time.sleep(3)
        test_facility_page.show_user_filter()
        time.sleep(3)
        test_facility_page.filter_user_input_element = 'SPAS_TEST SUPER_USER'
        time.sleep(3) 
        self.assertTrue(test_facility_page.user_access_is_granted(), 'Failed granting explicit facility access')
          

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()