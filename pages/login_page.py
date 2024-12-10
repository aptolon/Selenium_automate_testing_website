from selenium.webdriver.common.by import By
from core.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    EMAIL_FIELD = (By.ID, "field-5")
    PASSWORD_FIELD = (By.ID, "field-6")
    
    SUBMIT_BUTTON = (By.CSS_SELECTOR, ".envelope__footer .bar__button.button--solid")

    SUCCESS_MESSAGE = (By.CLASS_NAME, "h3")

    ERROR_MESSAGE = (By.CLASS_NAME, "jGrowl-message") 

    def login(self, email: str, password: str):
        self.enter_text(self.EMAIL_FIELD, email)
        self.enter_text(self.PASSWORD_FIELD, password)
        
        self.click_element(self.SUBMIT_BUTTON)

    def get_success_message(self) -> str:
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
            )
            return self.get_element_text(self.SUCCESS_MESSAGE)
        except Exception as e:
            print(f"Не удалось получить сообщение об успехе: {e}")
            return ""
    def get_error_message(self) -> str:
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            )
            return self.get_element_text(self.ERROR_MESSAGE)
        except Exception as e:
            print(f"Не удалось получить сообщение об ошибке: {e}")
            return ""

