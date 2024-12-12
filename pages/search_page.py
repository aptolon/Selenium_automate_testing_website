from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from core.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage(BasePage):
    """Page Object для функционала поиска."""

    SEARCH_ICON = (By.CLASS_NAME, 'search-opened-invisible')
    SEARCH_INPUT = (By.ID, "field-4")  # Локатор строки поиска
    SEARCH_RESULTS = (By.ID, 'search-result-products')

    def open_search_input(self):
        """Открытие строки поиска."""
        self.click_element(self.SEARCH_ICON)

    def enter_search_query(self, query):
        """Ввод текста в строку поиска."""
        self.open_search_input()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )
        
        self.enter_text(self.SEARCH_INPUT, query)

    def submit_search(self):
        """Отправка формы поиска (нажатие Enter)."""
        search_input = self.find_element(self.SEARCH_INPUT)
        if search_input:
            search_input.send_keys(Keys.RETURN)

    def get_search_results(self):
        """Получение результатов поиска."""
        return self.driver.find_elements(*self.SEARCH_RESULTS)

    def is_search_result_present(self, text):
        """Проверка наличия конкретного текста в результатах."""
        results = self.get_search_results()
        return any(text.lower() in result.text.lower() for result in results)
