from selenium.webdriver.common.by import By

class ViewFacilityPageLocators(object):
    FAC_PROD_TAB = (By.XPATH, "(//a[normalize-space()='Facility Products'])[1]")
    USERS_TAB = (By.XPATH, "(//a[normalize-space()='Users'])[1]")
    SHOW_IMPORT_PROD_POPUP = (By.XPATH, "(//div[@class='add-item-btn'])[1]")
    IMPORT_PROD_BUTTON = (By.XPATH, "(//span[@class='ficon ficon-in force-link async-target'])[2]")
    PRODS_ARE_SAVED = (By.XPATH, "//body/div/div/main/section/section/section/div/div/div/div/div/div/ul/li[1]/span[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
    OPTIONS_BUTTON = (By.XPATH, "(//span[contains(@class,'ficon ficon-more-vertical')])[2]")
    GRANT_FAC_ACCESS_BUTTON = (By.XPATH, "(//span[normalize-space()='Grant user access'])[1]")
    GRANT_ACCESS_SWITCH = (By.XPATH, "//body//div//section//div//main//div//div//ul//li//span//div//div//div//label//span")
    TEST_USER_ELEMENT = (By.XPATH, "(//div[@class='txt-blue txt-bold'])[1]")
    CLOSE_GRANT_ACCESS_POPUP = (By.XPATH, "(//span[contains(@class,'async-target ficon ficon-cross')])[1]")
    TEST_USER_LOCATED = (By.XPATH, "(//span[contains(@class,'accent-title link')])[1]")
    SHOW_USER_FILTER = (By.XPATH, "(//span[contains(@class,'async-target')])[11]")