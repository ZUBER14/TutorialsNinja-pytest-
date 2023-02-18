from selenium.webdriver.common.by import By

from PageObjects import LoginPageObjects


class ForgetPasswordPageObjects:

    def __init__(self, driver):
        self.driver = driver

    emailfield_loc = (By.ID, "input-email")
    continueButton_loc = (By.CSS_SELECTOR, "input[type=submit]")

    def emailAddress(self):
        return self.driver.find_element(*self.emailfield_loc)

    def continueButton(self):
        self.driver.find_element(*self.continueButton_loc).click()
        loginPage = LoginPageObjects.LoginPageObjects(self.driver)
        return loginPage

    # WARNING MESSAGES
    Warning_Emailaddress_war = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")
    forgetPasstext = (By.XPATH, "//div[@id='content']/h1")

    def WarningEmailAddress_Actual_Text(self):
        return self.driver.find_element(*self.Warning_Emailaddress_war).text

    def WarningEmailAddress_Expected_Text(self):
        return self.driver.find_element(*self.forgetPasstext).text

    def WarningEmailAddressField_Expected_Text(self):
        return "E-Mail must be between 4 and 20 characters!' should be displayed for 'E-Mail Address' field"

    # EXPECTED TEXT FOR ASSERTION
    def forgetPasstext_expected_text(self):
        return self.driver.find_element(*self.forgetPasstext).text

    # ACTUAL TEXT FOR ASSERTION
    def forgetPasstext_actual_text(self):
        return "Forgot Your Password?"
