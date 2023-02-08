from selenium.webdriver.common.by import By

class CreateUserPageLocators(object):
    USER_ROLE_SELECT = (By.XPATH, "(//select[@class='validation-ignore form-control'])[1]")
    PASSWORD_TAB = (By.XPATH, "(//a[normalize-space()='Password'])[1]")
    EMPLOYEE_IN_WRAPER = (By.XPATH, "(//div[contains(text(),'CM2W')])[1]")
    EMPLOYEE_IN_ORGANIZATION_ENTITY = (By.XPATH, "(//li[normalize-space()='SPAS_TEST_ORGANIZATION'])[1]")
    USER_IS_SAVED = (By.XPATH, "(//h1[normalize-space()='View User'])[1]")