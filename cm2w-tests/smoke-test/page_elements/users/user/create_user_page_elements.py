from element import BasePageElementByXpath


class UserFirstNameInputElement(BasePageElementByXpath):

    #The locator for user first name input
    locator = "(//input[@type='text'])[1]"

class UserLastNameInputElement(BasePageElementByXpath):

    #The locator for user last name input
    locator = "(//input[@type='text'])[2]"

class UserEmailInputElement(BasePageElementByXpath):

    #The locator for user email input
    locator = "(//input[@type='email'])[1]"

class UserEmployeeInInputElement(BasePageElementByXpath):
    """This class gets the search text from the specified locator"""

    #The locator for user role input
    locator = "(//input[@type='text'])[4]"

class UserPasswordInputElement(BasePageElementByXpath):
    """This class gets the search text from the specified locator"""

    #The locator for user role input
    locator = "(//input[@id='inputPassword'])[1]"

class UserConfirmPasswordInputElement(BasePageElementByXpath):
    """This class gets the search text from the specified locator"""

    #The locator for user role input
    locator = "(//input[@id='inputPasswordConfirm'])[1]"