from selenium.webdriver.common.by import By

class FacilitiesViewLocators(object):
    SEARCH_TEST_FACILITY_RESULT = (By.XPATH, "(//h3[contains(@class,'accent-title link')][normalize-space()='SPAS_TEST_FACILITY'])[1]")