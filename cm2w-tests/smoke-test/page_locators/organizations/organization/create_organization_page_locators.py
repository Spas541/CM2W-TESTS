from selenium.webdriver.common.by import By

class CreateOrganizationPageLocators(object):
    ORGANIZATION_DOMAIN_SELECT = (By.XPATH, "//select[@class='validation-ignore form-control']")
    ORGANIZATION_CURRENCY_SELECT = (By.XPATH, "(//select[@class='validation-ignore form-control'])[2]")
    PREFERENCES_TAB = (By.XPATH, "//a[contains(text(),'Preferences')]")
    ORGANIZATION_IS_SAVED_LOCATOR = (By.XPATH, "(//div[@class='add-item-btn access-class-org-create'])[1]")
    SUB_ORGANIZATION_IS_SAVED_LOCATOR = (By.XPATH, "(//span[normalize-space()='SPAS_TEST_SUB_ORGANIZATION'])[1]")