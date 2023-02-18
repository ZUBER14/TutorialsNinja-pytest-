import time

import pytest

from PageObjects.HomePageObjects import HomePageObjects
from Utilities.BaseClass import BaseClass
from testData.RegisterPageTestData import RegisterPageTestData


class TestRegister(BaseClass):

    def test_verify_Registering_Mandatory_Field(self, DataOfRegisterPage):
        log = self.getLogger()
        log.info("Script started to execute")
        homepage = HomePageObjects(self.driver)
        registerPage = homepage.Account_register()
        log.info("Giving all the necessary details into field")
        registerPage.firstName().send_keys(DataOfRegisterPage["firstName"])
        registerPage.lastName().send_keys(DataOfRegisterPage["lastName"])
        registerPage.email().send_keys(self.generate_email_with_time_stamp())
        registerPage.telephone().send_keys(DataOfRegisterPage["telephoneNumber"])
        registerPage.password().send_keys(DataOfRegisterPage["validPassword"])
        registerPage.confirmPassword().send_keys(DataOfRegisterPage["validConfirmPass"])
        registerPage.privacy_policy().click()
        accountConfirmPage = registerPage.submit()
        assert accountConfirmPage.confirm_account_created() == accountConfirmPage.conf_message()
        log.info("Account is created and Expected result and actual result is same")

    def test_verify_Registering_BY_Providing_All_Fileds(self, DataOfRegisterPage):
        log = self.getLogger()
        log.info("Script started to execute")
        homepage = HomePageObjects(self.driver)
        registerPage = homepage.Account_register()
        log.info("Giving all the necessary details into field")
        registerPage.firstName().send_keys(DataOfRegisterPage["firstName"])
        registerPage.lastName().send_keys(DataOfRegisterPage["lastName"])
        registerPage.email().send_keys(self.generate_email_with_time_stamp())
        registerPage.telephone().send_keys(DataOfRegisterPage["telephoneNumber"])
        registerPage.password().send_keys(DataOfRegisterPage["validPassword"])
        registerPage.confirmPassword().send_keys(DataOfRegisterPage["validConfirmPass"])
        registerPage.newsletter_YES().click()
        registerPage.privacy_policy().click()
        accountConfirmPage = registerPage.submit()

        assert accountConfirmPage.confirm_account_created() == accountConfirmPage.conf_message()
        log.info("Account is created and Expected result and actual result is same")

    def test_verify_Notification_BY_NotProviding_All_Fileds_BySubmiting(self):
        log = self.getLogger()
        log.info("Script started to execute")
        homepage = HomePageObjects(self.driver)
        registerPage = homepage.Account_register()
        registerPage.submit()

        log.warning("Warning messages on page")
        assert registerPage.firstName_actual_WarningMessage() == registerPage.firstName_exepected_WarningMessage()
        assert registerPage.lastName_actual_WarningMessage() == registerPage.lastName_exepected_WarningMessage()
        assert registerPage.email_actual_WarningMessage() == registerPage.email_exepected_WarningMessage()
        assert registerPage.telephone_actual_WarningMessage() == registerPage.telephone_exepected_WarningMessage()
        assert registerPage.password_actual_WarningMessage() == registerPage.password_exepected_WarningMessage()
        assert registerPage.privacyPolicy_actual_WarningMessage() == registerPage.privacyPolicy_exepected_WarningMessage()

    @pytest.fixture(params=RegisterPageTestData.RegisterPageTestData)
    def DataOfRegisterPage(self, request):
        return request.param
