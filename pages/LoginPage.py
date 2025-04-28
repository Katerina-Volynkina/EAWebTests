from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    LOGIN_PASSWORD = (By.ID, 'field_password')
    LOGIN_QR = (By.XPATH, '//*[@data-l="t,get_qr"]')
    LOGIN_CHECKIN = (By.XPATH, '//*[@data-l="t,register"]')
    LOGIN_ENTER = (By.XPATH, '//*[@data-l="t,login_tab"]')
    LOGIN_QR_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_RESTORE = (By.XPATH, '//*[@data-l="t,restore"]')
    LOGIN_NOT_PROFILE = (By.XPATH, '//*[@class="external-oauth-login_title-tx"]')
    LOGIN_ICON_VK = (By.XPATH, '//*[@class ="i ic social-icon __s __vk_id"]')
    LOGIN_ICON_MAILRU = (By.XPATH, '//*[@class="i ic social-icon __s __mailru"]')
    LOGIN_ICON_GP = (By.XPATH, '//*[@class ="i ic social-icon __s __gp"]')
    LOGIN_ICON_YANDEX = (By.XPATH, '//*[@class="i ic social-icon __s __yandex"]')
    LOGIN_ICON_APPLE = (By.XPATH, '//*[@class="i ic social-icon __s __apple"]')
class LoginPageHelper(BasePage):
    pass
