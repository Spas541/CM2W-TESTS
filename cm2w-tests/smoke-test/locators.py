from selenium.webdriver.common.by import By


class EntityPageLocators(object):
    CREATE_ENTITY_BUTTON  = (By.XPATH, "//span[@class='async-target ficon ficon-plus']")
    SAVE_ENTITY_BUTTON = (By.XPATH, "//span[@class='async-target ficon ficon-check']")


class CreateUserPageLocators(object):
    USER_ROLE_SELECT = (By.XPATH, "(//select[@class='validation-ignore form-control'])[1]")
    PASSWORD_TAB = (By.XPATH, "(//a[normalize-space()='Password'])[1]")

    

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    pass