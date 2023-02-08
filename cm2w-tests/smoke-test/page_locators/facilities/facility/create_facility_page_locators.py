from selenium.webdriver.common.by import By


class CreateFacilityPageLocators(object):
    FACILITY_IS_SAVED_LOCATOR = (By.XPATH, "(//div[@class='add-item-btn access-class-dev-create'])[1]")
    ORGANIZATION_IN_WRAPER = (By.XPATH, "(//div[@class='form-control'])[1]")
    ORGANIZATION_ENTITY = (By.XPATH, "(//li[normalize-space()='SPAS_TEST_ORGANIZATION'])[1]")