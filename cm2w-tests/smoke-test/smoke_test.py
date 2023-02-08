import unittest
from test_cases.create_entity_tests.create_device_test import CreateDeviceTest
from test_cases.create_entity_tests.create_org_test import CreateOrgTest
from test_cases.create_entity_tests.create_facility_test import CreateFacilityTest
from test_cases.create_entity_tests.create_user_test import CreateUserTest
from test_cases.create_entity_tests.create_org_product_test import CreateOrgProductTest
from facility_actions_test import FacilityActionsTest
from test_cases.create_entity_tests.create_not_template_test import CreateNotTemplateTest






if __name__ == "__main__":
    tc1 = unittest.TestLoader().loadTestsFromTestCase(CreateOrgTest)
    tc2 = unittest.TestLoader().loadTestsFromTestCase(CreateUserTest)
    tc3 = unittest.TestLoader().loadTestsFromTestCase(CreateFacilityTest)
    tc4 = unittest.TestLoader().loadTestsFromTestCase(CreateDeviceTest)
    tc5 = unittest.TestLoader().loadTestsFromTestCase(CreateOrgProductTest)
    tc6 = unittest.TestLoader().loadTestsFromTestCase(FacilityActionsTest)
    tc7 = unittest.TestLoader().loadTestsFromTestCase(CreateNotTemplateTest)

    SmokeTestSuite = unittest.TestSuite([tc1,tc2,tc3,tc4,tc5,tc6,tc7])
    unittest.TextTestRunner().run(SmokeTestSuite)