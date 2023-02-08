from selenium.webdriver.common.by import By

class HomePageLocators(object):
    ORGANIZATIONS_MENU_BUTTON = (By.ID, "organizations")
    USERS_MENU_BUTTON = (By.ID, "users")
    FACILITIES_MENU_BUTTON = (By.ID, "facilities")
    DEVICES_MENU_BUTTON = (By.ID, "devices")
    USER_ICON = (By.XPATH,"//span[@class='ficon ficon-user']")