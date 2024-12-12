from selenium.webdriver.common.by import By
from core.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FiltersPage(BasePage):
    # Локаторы
    FILTER_BAR_OPENER = (By.CSS_SELECTOR, "button[data-filter-bar-opener]")
    INSTOCK_FILTER_CHECKBOX = (By.XPATH, "//div[@data-swtchbx-root='sidebar']//span[contains(text(),'В интернет-магазине')]/parent::label")
    # RED_COLOR_CHECKBOX = (By.XPATH, "//li[@title='Красный']//label[contains(@class, 'checkbox')]//input[@type='checkbox' and @value='Red']")


    # COLORS_CONTAINER = (By.XPATH, "//span[@class='checkbox__switch donut donut--color']/span[@class='donut__bg checkbox__bg']")    

    RESET_FILTER_BUTTON = (By.XPATH, "//button[contains(@class, 'iconed__text')]")
    FILTER_RESULTS_COUNT = (By.CSS_SELECTOR, "span[data-shop-pager-total]")

    FILTER_OPTION = (By.CSS_SELECTOR, "li.swatch.is-sorted.tooltipstered")
    PRODUCT_COLOR_NAME = (By.CSS_SELECTOR, "div.card__subtitle.text--light.color-name[data-card-subtitle]")


    #color--red color--


    def open_filters_bar(self):
        """Открыть панель фильтров."""
        self.click_element(self.FILTER_BAR_OPENER)

    def select_instock_filter(self):
        self.open_filters_bar()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.INSTOCK_FILTER_CHECKBOX))

        
        self.click_element(self.INSTOCK_FILTER_CHECKBOX)

    def get_total_items(self):
        """Получить количество товаров."""
        return self.get_element_text(self.FILTER_RESULTS_COUNT)

    def select_filter_option_by_index(self, index):
        filter_options = self.find_elements(self.FILTER_OPTION)
        if 0 <= index < len(filter_options):
            filter_options[index].click()
        else:
            raise IndexError(f"Фильтр с индексом {index} не найден.")
        

    # def reset_filters(self):
    #     reset_button = WebDriverWait(self.driver, 50).until(
    #         EC.presence_of_element_located(self.RESET_FILTER_BUTTON)
    #     )
    #     # Проверка видимости элемента
    #     if not reset_button.is_displayed():
    #         print("Кнопка скрыта.")
    #     if not reset_button.is_enabled():
    #         print("Кнопка не активна.")

    def get_all_displayed_colors(self):

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.PRODUCT_COLOR_NAME)
        )
        elements = self.find_elements(self.PRODUCT_COLOR_NAME)
        return [element.text.strip() for element in elements if element.text.strip()]
