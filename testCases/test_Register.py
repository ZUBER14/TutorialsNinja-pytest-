import pytest

from PageObjects.HomePageObjects import HomePageObjects
from Utilities.BaseClass import BaseClass
from testData.RegisterPageTestData import RegisterPageTestData


class TestRegister(BaseClass):

    def test_verify_Registering_Mandatory_Field(self, DataOfRegisterPage):
        homepage = HomePageObjects(self.driver)
        registerPage = homepage.Account_register()
        registerPage.firstName().send_keys(DataOfRegisterPage["firstName"])
        registerPage.lastName().send_keys(DataOfRegisterPage["lastName"])
        registerPage.email().send_keys(self.generate_email_with_time_stamp())
        registerPage.telephone().send_keys(DataOfRegisterPage["telephoneNumber"])
        registerPage.password().send_keys(DataOfRegisterPage["validPassword"])
        registerPage.confirmPassword().send_keys(DataOfRegisterPage["validConfirmPass"])
        registerPage.privacy_policy().click()
        accountConfirmPage = registerPage.submit()

        assert accountConfirmPage.confirm_account_created() == accountConfirmPage.conf_message()

    @pytest.fixture(params=RegisterPageTestData.RegisterPageTestData)
    def DataOfRegisterPage(self, request):
        return request.param
