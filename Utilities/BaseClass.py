import datetime

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import datetime


@pytest.mark.usefixtures("setup")
class BaseClass:

    # def __init__(self, driver):
    #     self.driver = driver

    def generate_email_with_time_stamp(self):
        timestamp = datetime.datetime.now().strftime('%a_%b_%d_%H_%M_%S_%Z_%Y').replace(' ', '_').replace(':', '_')
        return "amotoori" + timestamp + "@gmail.com"

    def explicitlyWait(self, locator):
        wait = WebDriverWait(self.driver, 10, ignored_exceptions=[Exception]).until(
            EC.presence_of_element_located((locator)))
        return wait

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((text)))

    def explicitly_wait_for_element(self, by, value):
        wait = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by, value))
        return wait

