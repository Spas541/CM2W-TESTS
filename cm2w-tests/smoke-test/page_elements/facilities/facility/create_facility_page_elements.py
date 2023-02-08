from element import BasePageElementByXpath,BasePageElement

class FacilityNameInputElement(BasePageElementByXpath):

    #The locator for facility name input
    locator = "(//input[@type='text'])[1]"

class OrganizationNameInputElement(BasePageElementByXpath):

    #The locator for facility name input
    locator = "(//input[@type='text'])[3]"