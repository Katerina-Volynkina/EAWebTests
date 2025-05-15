import allure
from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_QR = (By.XPATH, '//*[@data-l="t,get_qr"]')
    REGISTRATION_BUTTON = (By.XPATH, '//div[@class="external-oauth-login-footer"]/a[@data-l="t,register"]')
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    LOGIN_QR_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    RESTORE_LINK = (By.XPATH, '//*[@data-l="t,restore"]')
    LOGIN_NOT_PROFILE = (By.XPATH, '//*[@class="external-oauth-login_title-tx"]')
    LOGIN_ICON_VK = (By.XPATH, '//*[@class ="i ic social-icon __s __vk_id"]')
    LOGIN_ICON_MAILRU = (By.XPATH, '//*[@class="i ic social-icon __s __mailru"]')
    LOGIN_ICON_GP = (By.XPATH, '//*[@class ="i ic social-icon __s __gp"]')
    LOGIN_ICON_YANDEX = (By.XPATH, '//*[@class="i ic social-icon __s __yandex"]')
    LOGIN_ICON_APPLE = (By.XPATH, '//*[@class="i ic social-icon __s __apple"]')
    ERROR_TEXT = (By.XPATH, '//*[@class="input-e login_error"]')
    GO_BACK_BUTTON = (By.XPATH, '//*[@data-l="t,cancel"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@class="external-oauth-login-help portlet_f"]')
    PROFILE_RECOVERY_BUTTON = (By.NAME, 'st.go_to_recovery')
class LoginPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()
    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_QR)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.LOGIN_QR_TAB)
        self.find_element(LoginPageLocators.RESTORE_LINK)
        self.find_element(LoginPageLocators.LOGIN_NOT_PROFILE)
        self.find_element(LoginPageLocators.LOGIN_ICON_VK)
        self.find_element(LoginPageLocators.LOGIN_ICON_MAILRU)
        self.find_element(LoginPageLocators.LOGIN_ICON_GP)
        self.find_element(LoginPageLocators.LOGIN_ICON_YANDEX)
        self.find_element(LoginPageLocators.LOGIN_ICON_APPLE)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step('Заполняем поле "Логин"')
    def type_login(self, login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()

    @allure.step('Заполняем поле "Пароль"')
    def type_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step('Переходим к восстановлению')
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.PROFILE_RECOVERY_BUTTON).click()

    @allure.step('Переходим к регистрации')
    def click_registration(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON).click()