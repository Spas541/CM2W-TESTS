from element import BasePageElement,BasePageElementByXpath

class EmailInputElement(BasePageElement):

    #The locator for user e-mail input
    locator = 'email'

class PasswordInputElement(BasePageElement):

    #The locator for user password input
    locator = 'pwd'