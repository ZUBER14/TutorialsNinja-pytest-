from selenium.webdriver.common.by import By


from PageObjects import LoginPageObjects, RegisterPageObjects
from Utilities.BaseClass import BaseClass


class HomePageObjects:
    baseClass = BaseClass()

    def __init__(self, driver):
        self.driver = driver

    account = (By.XPATH, "//span[text()='My Account']")
    register = (By.LINK_TEXT, "Register")
    login = (By.LINK_TEXT, "Login")

    def AccountDropdown(self):
        self.baseClass.wait_for_element(self.driver, self.account)
        return self.driver.find_element(*self.account)

    def selectRegister(self):
        return self.driver.find_element(*self.register)

    def selectLogin(self):
        return self.driver.find_element(*self.login)

    def Account_register(self):
        self.baseClass.wait_for_element(self.driver, self.account).click()
        # self.driver.find_element(*self.account).click()
        self.driver.find_element(*self.register).click()
        registerPage = RegisterPageObjects.RegisterPageObjects(self.driver)
        return registerPage

    def Account_login(self):
        self.baseClass.wait_for_element(self.driver, self.account)
        self.driver.find_element(*self.account).click()
        self.driver.find_element(*self.login).click()
        loginPage = LoginPageObjects.LoginPageObjects(self.driver)
        return loginPage

    # Assertion
    # ACTUAL TEXT ON HOMEPAGE FOR ASSERTION
    your_store = (By.LINK_TEXT, "Your Store")

    def YourStore_Actual_Text(self):
        return self.driver.find_element(*self.your_store).text

    def YourStore_Expected_Text(self):
        return "Your Store"
