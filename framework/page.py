from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located(locator)
        )
        return element

    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()
