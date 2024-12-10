from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            return None

    def click_element(self, locator):
        element = self.find_element(locator)
        if element:
            element.click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        if element:
            element.clear()
            element.send_keys(text)

    def get_element_text(self, locator):
        element = self.find_element(locator)
        if element:
            return element.text
        return ""
