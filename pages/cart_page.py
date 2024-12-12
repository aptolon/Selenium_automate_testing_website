from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.base_page import BasePage


class CartPage(BasePage):
    ADD_TO_CART_BUTTON = (By.NAME, "ms2_action")
    CART_ICON = (By.ID, "msMiniCart")
    REMOVE_ITEM_BUTTON = (By.XPATH, "//button[@value='cart/remove']")
    CART_TOTAL_PRICE = (By.XPATH, "//div[@class='pos__sum price']")
    CART_EMPTY_MESSAGE = (By.CLASS_NAME, "h3")
    PLUS_BUTTON = (By.XPATH, "//button[@class='quantity__btn' and @type='submit' and @data-quantity-plus]/div[@class='plus']")
    PROMOCODE_FIELD = (By.XPATH, "//input[@name='certificate']")
    APPLY_BUTTON = (By.XPATH, "//button[contains(@class, 'mspc_btn') and contains(@class, 'bar__button') and contains(@class, 'button') and span[text()='Применить']]")
    ERROR_MESSAGE = (By.CLASS_NAME, "jGrowl-message") 
    
    def add_item_to_cart(self):
        """Добавить товар в корзину."""

        self.click_element(self.ADD_TO_CART_BUTTON)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.CART_ICON)
        )

    def navigate_to_cart(self):
        """Перейти в корзину."""
        self.click_element(self.CART_ICON)

    def change_item_quantity(self, quantity):
        """Изменить количество товара в корзине."""
        for _ in range(quantity - 1):
            self.click_element(self.PLUS_BUTTON)

    def remove_item_from_cart(self):
        """Удалить товар из корзины."""
        self.click_element(self.REMOVE_ITEM_BUTTON)

    def get_total_price(self):
        """Получить общую сумму в корзине."""
        return self.get_element_text(self.CART_TOTAL_PRICE)

    def is_cart_empty(self):
        """Проверить, что корзина пуста."""
        element = self.find_element(self.CART_EMPTY_MESSAGE)
        return bool(element and "В вашей корзине пусто" in element.text)

    
    def enter_promocode(self, code):
        """Ввести промокод."""
        self.enter_text(self.PROMOCODE_FIELD, code)
        self.click_element(self.APPLY_BUTTON)
    def get_error_message(self) -> str:
        """Получить сообщение об ошибке регистрации."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            )
            return self.get_element_text(self.ERROR_MESSAGE)
        except Exception as e:
            print(f"Не удалось получить сообщение об ошибке: {e}")
            return ""
