from selenium.webdriver.common.by import By
from core.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NavigationPage(BasePage):
    BAGS_LINK = (By.LINK_TEXT, "Сумки")
    CONTACTS_LINK = (By.LINK_TEXT, "Контакты")
    FIND_STORE_LINK = (By.LINK_TEXT, "Найти магазин")
    # ACCESSORIES_LINK = (By.XPATH, "//li[contains(@class, 'header__menu-item') and contains(., 'Аксессуары')]")
    # JEWELRY_LINK = (By.XPATH, "//a[contains(@href, '/category/aksessuary/ukrasheniya-arny/')]")

    def navigate_to_bags(self):
        """Переход на страницу 'Сумки'."""
        self.click_element(self.BAGS_LINK)

    def navigate_to_contacts(self):
        """Переход на страницу 'Контакты'."""
        self.click_element(self.CONTACTS_LINK)

    def navigate_to_find_store(self):
        """Переход на страницу 'Найти магазин'."""
        self.click_element(self.FIND_STORE_LINK)

    # def navigate_to_jewelry(self):
    #     self.hover_element(self.ACCESSORIES_LINK)
        
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(self.JEWELRY_LINK)
    #     )
    #     self.click_element(self.JEWELRY_LINK)
