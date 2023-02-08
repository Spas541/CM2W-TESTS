from element import BasePageElement,BasePageElementByXpath

class SearchUserInputElement(BasePageElementByXpath):
    locator = "(//input[@placeholder='Search'])[1]"

class FilterUserInputElement(BasePageElementByXpath):
    locator = "(//input[@placeholder='User'])[1]"