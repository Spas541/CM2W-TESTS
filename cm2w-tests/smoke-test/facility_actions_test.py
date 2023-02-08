import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.login_page import LoginPage 
from pages.home_page import HomePage
from pages.facilities.facilities_view_page import FacilitiesPage
from pages.facilities.facility.view_facility_page import ViewFacilityPage

class FacilityActionsTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:4200")
        login_page = LoginPage(self.driver)
        login_page.email_input_element = 'stuhlov@cm2w.net'
        login_page.password_input_element = '@Stuhlov1234'
        
        login_page.click_login_button()
        
    def test_grant_user_explicit_facility_access(self):
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

    def test_import_product_to_fac(self):
        home_page = HomePage(self.driver)
        self.driver.maximize_window()
        self.assertTrue(home_page.is_loged_in(), 'Unsuccessfull LOGIN')
        self.assertTrue(home_page.goto_facilities(), 'Unsuccessfull routing to FACILITIES page')
        facilities_page = FacilitiesPage(self.driver)
        self.assertTrue(facilities_page.search_test_facility(), 'Test facility not found')
        facilities_page.goto_test_facility_view()
        test_facility_page = ViewFacilityPage(self.driver)
        test_facility_page.go_to_fac_prod_tab()
        test_facility_page.show_import_org_prod_popup()
        time.sleep(3)
        test_facility_page.import_org_prod()
        time.sleep(3)
        self.assertTrue(test_facility_page.prod_is_saved(), 'Unsuccessfull importing org product from parent org')
          

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()