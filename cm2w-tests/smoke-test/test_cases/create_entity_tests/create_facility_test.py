import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.login_page import LoginPage 
from pages.home_page import HomePage
from pages.facilities.facilities_view_page import FacilitiesPage
from pages.facilities.facility.create_facility_page import CreateFacilityPage



class CreateFacilityTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:4200")
        login_page = LoginPage(self.driver)
        login_page.email_input_element = 'stuhlov@cm2w.net'
        login_page.password_input_element = '@Stuhlov1234'
        
        login_page.click_login_button()
        

    def test_create_facility(self):
        home_page = HomePage(self.driver)
        self.assertTrue(home_page.is_loged_in(), 'Unsuccessfull LOGIN')
        self.assertTrue(home_page.goto_facilities(), 'Unsuccessfull routing to FACILITIES page')
        facilities_page = FacilitiesPage(self.driver)
        self.assertTrue(facilities_page.goto_create_facility(),'Unsuccessfull routing to create FACILITY page')
        create_facility_page = CreateFacilityPage(self.driver)
        create_facility_page.facility_name = 'SPAS_TEST_FACILITY'
        create_facility_page.select_test_organization()
        create_facility_page.save_facility()
        self.assertTrue(create_facility_page.facility_is_saved(), 'Error when saving the test FACILITY')
          

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()