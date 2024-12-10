from selenium.webdriver.common.by import By
from core.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage(BasePage):
    EMAIL_FIELD = (By.ID, "office-auth-register-email")
    MOBILE_PHONE_FIELD = (By.ID, "office-auth-register-mobilephone")
    PASSWORD_FIELD = (By.ID, "office-register-form-password")
    DOB_FIELD = (By.ID, "office-register-form-dob")
    GENDER_MALE_RADIO = (By.CSS_SELECTOR, "input[name='gender'][value='1'] + label")
    GENDER_FEMALE_RADIO = (By.CSS_SELECTOR, "input[name='gender'][value='2'] + label")
    POLICY_CHECKBOX = (By.CLASS_NAME, "checkbox--policy")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit'][data-analytics='register']")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "form__success-inner")

    ERROR_MESSAGE = (By.CLASS_NAME, "jGrowl-message") 

    def register(self, email: str, mobile_phone: str, password: str, gender: str, dob: str):
        """Регистрация нового пользователя."""
        self.enter_text(self.EMAIL_FIELD, email)
        self.enter_text(self.MOBILE_PHONE_FIELD, mobile_phone)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.enter_text(self.DOB_FIELD, dob)
        
        if gender == "male":
            self.click_element(self.GENDER_MALE_RADIO)
        elif gender == "female":
            self.click_element(self.GENDER_FEMALE_RADIO)

        self.click_element(self.POLICY_CHECKBOX)
        
        self.click_element(self.SUBMIT_BUTTON)

    def get_success_message(self) -> str:
        """Получить сообщение об успешной регистрации с ожиданием."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
            )
            return self.get_element_text(self.SUCCESS_MESSAGE)
        except Exception as e:
            print(f"Не удалось получить сообщение об успехе: {e}")
            return ""
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

