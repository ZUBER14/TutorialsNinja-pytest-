from selenium.webdriver.common.by import By


from PageObjects import AccountPageObjects


class PasswordPageObjects:

    def __init__(self, driver):
        self.driver = driver

    password_loc = (By.ID, "input-password")
    conf_password_loc = (By.ID, "input-confirm")
    continueButton_loc = (By.CSS_SELECTOR, "input[type='submit']")

    def password(self):
        return self.driver.find_element(*self.password_loc)

    def conf_password(self):
        return self.driver.find_element(*self.conf_password_loc)

    def continueButton(self):
        self.driver.find_element(*self.continueButton_loc).click()
        accountPage = AccountPageObjects.AccountPageObjects(self.driver)
        return accountPage
