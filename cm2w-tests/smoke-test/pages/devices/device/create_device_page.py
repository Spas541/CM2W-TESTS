from page import BasePage
from page_elements.devices.device.create_device_page_elements import DeviceFacilityInputElement, DeviceNameInputElement, DeviceSerialNumberInputElement
from page_locators.entity_page_locators import EntityPageLocators
from page_locators.devices.device.create_device_page_locators import CreateDevicePageLocators


class CreateDevicePage(BasePage):
    device_name = DeviceNameInputElement()
    device_sn = DeviceSerialNumberInputElement()
    device_facility = DeviceFacilityInputElement()

    def select_facility(self):
        wraper_element = self.driver.find_element(*CreateDevicePageLocators.SELECT_FACILITY_WRAPER)
        wraper_element.click()
        self.device_facility = 'SPAS_TEST_FACILITY'
        element = self.locate_element_by(CreateDevicePageLocators.TEST_FACILITY_ENTITY)
        self.click_element(element)


    def save_device(self):
        element = self.driver.find_element(*EntityPageLocators.SAVE_ENTITY_BUTTON)
        element.click()


    def device_is_saved(self):
        return self.locate_element_by(CreateDevicePageLocators.TEST_FACILITY_IS_SAVED)
        