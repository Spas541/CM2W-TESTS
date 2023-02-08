from element import BasePageElement,BasePageElementByXpath

class OrganizationNameInputElement(BasePageElementByXpath):

    #The locator for organization name input
    locator = "//div[@class='row']//div[1]//div[1]//div[1]//input[1]"