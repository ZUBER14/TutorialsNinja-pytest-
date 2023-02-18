from selenium.webdriver.common.by import By

from PageObjects import LoginPageObjects, RegisterPageObjects


class AccountConfirmPageObjects:

    def __init__(self, driver):
        self.driver = driver

    conf_account_loc = (By.XPATH, "//div[@id='content']/h1")
    continue_button_loc = (By.LINK_TEXT, "Continue")
    edit_account_loc = (By.LINK_TEXT, "Edit Account")

    def confirm_account_created(self):
        return self.driver.find_element(*self.conf_account_loc).text

    def continue_button(self):
        self.driver.find_element(*self.continue_button_loc)
        loginPage = LoginPageObjects.LoginPageObjects(self.driver)
        return loginPage

    def editAccount(self):
        self.driver.find_element(*self.edit_account_loc)
        registerPage = RegisterPageObjects.RegisterPageObjects(self.driver)
        return registerPage

    def conf_message(self):
        return "Your Account Has Been Created!"
