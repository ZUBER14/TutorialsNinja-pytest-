import datetime

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import datetime


@pytest.mark.usefixtures("setup")
class BaseClass:

    def generate_email_with_time_stamp(self):
        timestamp = datetime.datetime.now().strftime('%a_%b_%d_%H_%M_%S_%Z_%Y').replace(' ', '_').replace(':', '_')
        return "amotoori" + timestamp + "@gmail.com"

    def set_implicit_wait(self, driver, seconds):
        driver.implicitly_wait(seconds)

    def wait_for_element(self, driver, locator, timeout=10):
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.presence_of_element_located(locator))
        return element

