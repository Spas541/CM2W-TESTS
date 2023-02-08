from selenium.webdriver.common.by import By

class EntityPageLocators(object):
    CREATE_ENTITY_BUTTON  = (By.XPATH, "//span[@class='async-target ficon ficon-plus']")
    SAVE_ENTITY_BUTTON = (By.XPATH, "//span[@class='async-target ficon ficon-check']")