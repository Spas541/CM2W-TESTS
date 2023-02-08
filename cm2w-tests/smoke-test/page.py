from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver

    def locate_element_by(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except Exception as e:
            print(e)
            return False

    def click_element(self, element):
        try:
            element.click()
            return element
        except Exception as e :
            print(e)
            return element



