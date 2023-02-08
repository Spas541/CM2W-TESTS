from element import BasePageElement,BasePageElementByXpath


class NewOrgProdNameInput(BasePageElementByXpath):
    #The locator for org search input
    locator = "(//input[@type='text'])[1]"

class NewOrgProdPriceInput(BasePageElementByXpath):
    locator = "(//input[@type='number'])[2]"

class NewNotTemplateName(BasePageElementByXpath):
    locator = ("(//input[@class='form-control ember-text-field ember-view'])[1]")

class OrgProdsContainer(BasePageElementByXpath):
    locator = "(//ul[contains(@class,'list sep-items v-space')])[3]"