from selenium.webdriver.common.by import By

class ViewOrganizationPageLocators(object):
    ORG_PROD_TAB = (By.XPATH, "(//a[normalize-space()='Organization Products'])[1]")
    NOT_TEMPLATE_TAB = (By.XPATH, "(//a[normalize-space()='Notification templates'])[1]")
    ADD_PROD_BUTTON = (By.XPATH, "(//div[normalize-space()='Add Organization Product'])[1]")
    ADD_NOT_TEMPLATE_BUTTON = (By.XPATH, "(//div[@class='add-item-btn'])[1]")
    ADD_SUB_ORG_BUTTON = (By.XPATH, "(//div[contains(@class,'add-item-btn access-class-org-create')])[1]")
    SAVE_PROD_BUTTON = (By.XPATH, "//span[@class='async-target ficon ficon-check']")
    SAVE_TEMPLATE_BUTTON = (By.XPATH, "(//span[contains(text(),'Save')])[1]")
    PROD_IS_SAVED = (By.XPATH, "(//span[@class='ficon ficon-link force-link async-target'])[1]")
    NOT_TEMPLATE_LVL_SELECT = (By.XPATH, "(//select[@class='validation-ignore form-control'])[1]")
    NOT_TEMPLATE_IS_SAVED = (By.XPATH, "(//div[contains(@class,'accent-title link')])[1]")
    OPTIONS_BUTTON = (By.XPATH, "//div[contains(@class,'pan-actions')]//span[contains(@class,'ficon ficon-more-vertical')]")
    SHOW_IMPORT_ORG_PRODUCT_MODAL_BUTTON = (By.XPATH, "//span[normalize-space()='Import Product']")
    IMPORT_PROD_BUTTON = (By.XPATH, "(//span[contains(@class,'ficon ficon-in force-link async-target')])[2]")
    PROD_IS_IMPORTED = (By.XPATH, "(//div[contains(@class,'accent-title link pb-0 h-fit-content f-box vcbox gap-05')])[1]")
    ORG_PRODS_CONTAINER = (By.XPATH, "(//ul[contains(@class,'list sep-items v-space')])[3]")