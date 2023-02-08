from selenium.webdriver.common.by import By


class CreateDevicePageLocators(object):
    SELECT_FACILITY_WRAPER = (By.XPATH, "(//div[contains(text(),'Select Facility')])[1]")
    TEST_FACILITY_ENTITY = (By.XPATH, "(//li[normalize-space()='SPAS_TEST_FACILITY'])[1]")
    TEST_FACILITY_IS_SAVED = (By.XPATH, "(//span[normalize-space()='Schematic settings'])[1]")