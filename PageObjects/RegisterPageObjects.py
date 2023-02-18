from selenium.webdriver.common.by import By


from PageObjects import AccountConfirmPageObjects


class RegisterPageObjects:

    def __init__(self, driver):
        self.driver = driver

    firstName_loc = (By.ID, "input-firstname")
    lastName_loc = (By.ID, "input-lastname")
    email_loc = (By.ID, "input-email")
    telephone_loc = (By.ID, "input-telephone")
    password_loc = (By.ID, "input-password")
    conf_password_loc = (By.ID, "input-confirm")
    privacy_policy_loc = (By.CSS_SELECTOR, "input[name=agree]")
    submit_loc = (By.CSS_SELECTOR, "input[type=submit]")
    yes_loc = (By.XPATH, "(//div[@class='col-sm-10'])[8]/descendant::input[1]")
    no_loc = (By.XPATH, "(//div[@class='col-sm-10'])[8]/descendant::input[2]")

    def firstName(self):
        return self.driver.find_element(*self.firstName_loc)

    def lastName(self):
        return self.driver.find_element(*self.lastName_loc)

    def email(self):
        return self.driver.find_element(*self.email_loc)

    def telephone(self):
        return self.driver.find_element(*self.telephone_loc)

    def password(self):
        return self.driver.find_element(*self.password_loc)

    def confirmPassword(self):
        return self.driver.find_element(*self.conf_password_loc)

    def privacy_policy(self):
        return self.driver.find_element(*self.privacy_policy_loc)

    def submit(self):
        self.driver.find_element(*self.submit_loc).click()
        accountConfirmPage = AccountConfirmPageObjects.AccountConfirmPageObjects(self.driver)
        return accountConfirmPage

    def newsletter_YES(self):
        return self.driver.find_element(*self.yes_loc)

    def newsletter_NO(self):
        return self.driver.find_element(*self.no_loc)

    # ACTUAL WARNING MESSAGES
    firstname_warn = (By.XPATH, "//input[@id='input-firstname']/following::div[1]")
    lastname_warn = (By.XPATH, "//input[@id='input-lastname']/following::div[1]")
    email_warn = (By.XPATH, "//input[@id='input-email']/following::div[1]")
    telephone_warn = (By.XPATH, "//input[@id='input-telephone']/following::div[1]")
    password_warn = (By.XPATH, "//input[@id='input-password']/following::div[1]")
    confPassword_warn = (By.XPATH, "//input[@id='input-confirm']/following::div[1]")
    privacyPolicy_warn = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")
    loginPage_warn = (By.XPATH, "//div[@id='content']/p")
    alreadyRegistered_warn = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")

    def firstName_actual_WarningMessage(self):
        return self.driver.find_element(*self.firstname_warn).text

    def lastName_actual_WarningMessage(self):
        return self.driver.find_element(*self.lastname_warn).text

    def email_actual_WarningMessage(self):
        return self.driver.find_element(*self.email_warn).text

    def telephone_actual_WarningMessage(self):
        return self.driver.find_element(*self.telephone_warn).text

    def password_actual_WarningMessage(self):
        return self.driver.find_element(*self.password_warn).Text()

    def confirmPass_actual_WarningMessage(self):
        return self.driver.find_element(*self.confPassword_warn).text

    def privacyPolicy_actual_WarningMessage(self):
        return self.driver.find_element(*self.privacyPolicy_warn).text

    def loginpage_actual_WarningMessage(self):
        return self.driver.find_element(*self.loginPage_warn).text

    def alreadyRegistered_actual_WarningMessage(self):
        return self.driver.find_element(*self.alreadyRegistered_warn).text

    # EXPECTED WARNING MESSAGES

    def firstName_exepected_WarningMessage(self):
        return "First Name must be between 1 and 32 characters!"

    def lastName_exepected_WarningMessage(self):
        return "Last Name must be between 1 and 32 characters!"

    def Email_exepected_WarningMessage(self):
        return "E-Mail Address does not appear to be valid!"

    def Telephone_exepected_WarningMessage(self):
        return "Telephone must be between 3 and 32 characters!"

    def Password_exepected_WarningMessage(self):
        return "Password must be between 4 and 20 characters!"

    def ConfirmPass_expected_WarningMessage(self):
        return "Password confirmation does not match password!"

    def PrivacyPolicy_exepected_WarningMessage(self):
        return "Warning: You must agree to the Privacy Policy!"

    def LoginPage_expected_WarningMessage(self):
        return "If you already have an account with us, please login at the login page."

    def alreadyRegistered_expected_WarningMessage(self):
        return "Warning: E-Mail Address is already registered!"

    def passwordComplexity_expected_WarningMessage(self):
        return "password should contain atleat one number, symbol, lower case letter and upper case letters"
