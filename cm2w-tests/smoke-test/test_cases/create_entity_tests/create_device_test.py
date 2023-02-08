import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.login_page import LoginPage 
from pages.home_page import HomePage
from pages.devices.devices_view_page import DevicesPage
from pages.devices.device.create_device_page import CreateDevicePage


class CreateDeviceTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:4200")
        login_page = LoginPage(self.driver)
        login_page.email_input_element = 'stuhlov@cm2w.net'
        login_page.password_input_element = '@Stuhlov1234'
        
        login_page.click_login_button()

    def test_create_device(self):
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
          

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()