import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.login_page import LoginPage 
from pages.home_page import HomePage
from pages.users.users_view_page import UsersPage
from pages.users.user.create_user_page import CreateUserPage


class CreateUserTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:4200")
        login_page = LoginPage(self.driver)
        login_page.email_input_element = 'stuhlov@cm2w.net'
        login_page.password_input_element = '@Stuhlov1234'
        
        login_page.click_login_button()
        
    def test_create_user(self):
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
          

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()