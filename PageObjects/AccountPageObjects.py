from selenium.webdriver.common.by import By

from PageObjects import PasswordPageObjects, LogoutPageObjects
from Utilities.BaseClass import BaseClass


class AccountPageObjects:

    def __init__(self, driver):
        self.driver = driver

    baseClass = BaseClass()

    # PAGE OBJECTS
    password_loc = (By.LINK_TEXT, "Password")
    logout_OnPage_loc = (By.LINK_TEXT, "Logout")

    def Change_Password(self):
        self.driver.find_element(*self.password_loc)
        passwordPage = PasswordPageObjects.PasswordPageObjects(self.driver)
        return passwordPage

    def Logout_OnPage(self):
        self.driver.find_element(*self.logout_OnPage_loc)
        logoutPage = LogoutPageObjects.LogoutPageObjects(self.driver)
        return logoutPage

    # ACCOUNT DROPDOWN OBJECTS
    accountDropdown_loc = (By.XPATH, "//span[text()='My Account']")
    logout_Dropdown_loc = (By.LINK_TEXT, "Logout")

    def MyAccountDropdown_LoginPage(self):
        self.baseClass.wait_for_element(self.driver, self.accountDropdown_loc)
        return self.driver.find_element(*self.accountDropdown_loc)

    def Logout_LoginPage(self):
        self.baseClass.wait_for_element(self.driver, self.accountDropdown_loc)
        self.driver.find_element(*self.logout_Dropdown_loc).click()
        logoutPage = LogoutPageObjects.LogoutPageObjects(self.driver)
        return logoutPage

    # TEXT FOR ASSERTION
    myAccount = (By.XPATH, "//div[@id='content']/h2[1]")

    def myAccount_Actual_Text(self):
        return self.driver.find_element(*self.myAccount).text

    def myAccountText_Expected_Text(self):
        return "My Account"

    # ACTUAL WARNING MESSAGES
    password_war = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def changePassword_actual_WarningMessage(self):
        return self.driver.find_element(*self.password_war).text

    # EXPECTED WARNING MESSAGES
    def changePassword_exepected_WarningMessage(self):
        return "Success: Your password has been successfully updated."
