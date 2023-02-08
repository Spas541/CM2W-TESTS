from element import BasePageElement,BasePageElementByXpath


class FacilitySearchNameInputElement(BasePageElementByXpath):
    #The locator for org search input
    locator = "(//input[@placeholder='Search'])[1]"