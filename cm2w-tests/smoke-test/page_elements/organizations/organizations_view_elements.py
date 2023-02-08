from element import BasePageElement,BasePageElementByXpath


class OrganizationSearchNameInputElement(BasePageElementByXpath):
    #The locator for org search input
    locator = "(//input[@placeholder='Search'])[1]"