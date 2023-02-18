import datetime
import inspect
import logging

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def generate_email_with_time_stamp(self):
        timestamp = datetime.datetime.now().strftime('%a_%b_%d_%H_%M_%S_%Z_%Y').replace(' ', '_').replace(':', '_')
        return "amotoori" + timestamp + "@gmail.com"

    def set_implicit_wait(self, driver, seconds):
        driver.implicitly_wait(seconds)

    def wait_for_element(self, driver, locator, timeout=10):
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.presence_of_element_located(locator))
        return element
