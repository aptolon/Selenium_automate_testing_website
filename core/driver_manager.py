from selenium import webdriver


from selenium import webdriver

class DriverManager:
    @staticmethod
    def get_driver(browser="chrome"):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            return webdriver.Chrome(options=options)
        else:
            raise ValueError(f"Браузер {browser} не поддерживается.")



# def test_driver_manager():
#     try:
#         driver = DriverManager.get_driver()
#         driver.get("https://arnypraht.com/")
#         assert "ARNY PRAHT официальный интернет-магазин дизайнерских женских сумок из экокожи" in driver.title 
#         print("DriverManager работает корректно.")
#     except Exception as e:
#         print(f"DriverManager не прошел проверку: {e}")
#     finally:
#         driver.quit()

# test_driver_manager()