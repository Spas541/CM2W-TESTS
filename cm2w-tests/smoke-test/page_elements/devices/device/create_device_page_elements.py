from element import BasePageElementByXpath, BasePageElement


class DeviceNameInputElement(BasePageElementByXpath):

    #The locator for device name input
    locator = "(//input[@type='text'])[5]"

class DeviceFacilityInputElement(BasePageElementByXpath):

    #The locator for device facility name input
    locator = "(//input[@type='text'])[2]"

class DeviceSerialNumberInputElement(BasePageElementByXpath):

    #The locator for sn input 
    locator = "(//input[@type='text'])[3]"
