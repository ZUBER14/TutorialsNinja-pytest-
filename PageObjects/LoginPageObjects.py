from selenium.webdriver.common.by import By

from PageObjects import AccountPageObjects, RegisterPageObjects, ForgetPasswordPageObjects
from Utilities.BaseClass import BaseClass


class LoginPageObjects:

    def __init__(self, driver):
        self.driver = driver

    baseClass = BaseClass()

    # WEB ELEMENT OF PAGE
    email_loc = (By.ID, "input-email")
    password_loc = (By.ID, "input-password")
    login_loc = (By.XPATH, "//input[@type='submit']")
    newCustomer_Continue_loc = (By.LINK_TEXT, "Continue")

    def Email(self):
        return self.driver.find_element(*self.email_loc)

    def password(self):
        return self.driver.find_element(*self.password_loc)

    def Login(self):
        self.driver.find_element(*self.login_loc).click()
        accountPage = AccountPageObjects.AccountPageObjects(self.driver)
        return accountPage

    def newCustomer_Continue(self):
        self.driver.find_element(self.newCustomer_Continue_loc)
        registerPage = RegisterPageObjects.RegisterPageObjects(self.driver)
        return registerPage

    # SIDE COLUMN WEB ELEMENT
    forgetPassword_loc = (By.LINK_TEXT, "Forgotten Password")
    Logout_sideColumn_loc = (By.XPATH, "//div[@class='list-group']//a[text()='Logout']")

    def ForgetPassword(self):
        self.driver.find_element(*self.forgetPassword_loc).click()
        forgetPassword = ForgetPasswordPageObjects.ForgetPasswordPageObjects(self.driver)
        return forgetPassword

    def Logout_sideColumn(self):
        return self.driver.find_element(*self.Logout_sideColumn_loc)

    def LoginToAccount(self, email, password):
        self.driver.find_element(*self.email_loc).send_keys(email)
        self.driver.find_element(*self.password_loc).send_keys(password)
        self.driver.find_element(*self.login_loc).click()
        accountPage = AccountPageObjects.AccountPageObjects(self.driver)
        return accountPage

    # ACCOUNT DROPDOWN WEB ELEMENTS
    AccountDropDown = (By.LINK_TEXT, "My Account")
    AccountDropDown_Forget = (By.XPATH, "(//a[contains(text(),'Logout')])[1]")

    def LoginPageDropDown(self):
        self.baseClass.wait_for_element(self.driver, self.AccountDropDown)
        self.driver.find_element(*self.AccountDropDown).click()
        return self.driver.find_element(*self.AccountDropDown_Forget)

    # HEADER PAGE WEB ELEMENT
    cameras_headers_loc = (By.LINK_TEXT, "Cameras")

    def cameras_headers(self):
        return self.driver.find_element(*self.cameras_headers_loc)

    # ACTUAL WARNING MESSAGES OF PAGE
    noMatch_warn = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")
    email_confirmation_forgetPass_warn = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def noMatch_actual_WarningMessage(self):
        return self.driver.find_element(*self.noMatch_warn).text

    def email_confirmation_forgetPass_actual_ConfirmationMessage(self):
        return self.driver.find_element(*self.email_confirmation_forgetPass_warn).text

    # EXPECTED WARNING MESSAGES OF PAGE

    def noMatch_exepected_WarningMessage(self):
        return "Warning: No match for E-Mail Address and/or Password."

    def email_confirmation_forgetPass_Expected_ConfirmationMessage(self):
        return "An email with a confirmation link has been sent your email address."

    # TEXT ON PAGE FOR ASSERTION
    returningCustomer_loc = (By.XPATH, "(//div[@class='well'])[2]/h2")

    def returningCustomer_actual_text(self):
        return self.driver.find_element(*self.returningCustomer_loc).text

    def returningCustomer_expected_text(self):
        return "Returning Customer"

    def exceeded_login_attempts_expected_warning(self):
        return "Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour."

    # MOVE TO CAMERA PAGE
    cameraText_loc = (By.XPATH, "//div[@id='content']/h2")

    def CameraText_actual_text(self):
        return self.driver.find_element(*self.cameraText_loc).text

    def CameraText_expected_text(self):
        return "Cameras"
