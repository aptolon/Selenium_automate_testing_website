from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    def find_elements(self, locator):
        return WebDriverWait(self.driver, 0).until(EC.presence_of_all_elements_located(locator))

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

    def hover_element(self, locator):
        element = self.find_element(locator)
        if element:
            ActionChains(self.driver).move_to_element(element).perform()
