from selenium.webdriver.common.by import By


from PageObjects import HomePageObjects, LoginPageObjects
from Utilities.BaseClass import BaseClass


class LogoutPageObjects:

    def __init__(self, driver):
        self.driver = driver

    baseClass = BaseClass()

    # PAGE OBJECTS
    Continue_loc = (By.LINK_TEXT, "Continue")

    def ContinueButton(self):
        self.driver.find_element(*self.Continue_loc).click()
        homepage = HomePageObjects.HomePageObjects(self.driver)
        return homepage

    # DROPDOWN ELEMENT IN LOGOUT PAGE
    account_loc = (By.XPATH, "//span[text()='My Account']")
    register_loc = (By.LINK_TEXT, "Register")
    login_loc = (By.LINK_TEXT, "Login")

    def Account_logout(self):
        self.baseClass.wait_for_element(self.driver, self.account_loc)
        self.driver.find_element(*self.account_loc).click()
        self.driver.find_element(*self.login_loc).click()
        loginPage = LoginPageObjects.LoginPageObjects(self.driver)
        return loginPage

    # ACTUAL TEXT FOR ASSERTION
    accountLogout_loc = (By.XPATH, "//div[@id='content']/h1")

    def AccountLogout_Actual_Text(self):
        return self.driver.find_element(*self.accountLogout_loc).text

    # EXPECTED TEXT FOR ASSERTION
    def AccountLogout_Expected_Text(self):
        return "Account Logout"
