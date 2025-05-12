import allure
from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.HelpPage import HelpPageHelper, HelpPageLocators


BASE_URL = 'http://ok.ru/help'


@allure.suite('Проверка ссылки Помощь')
@allure.title('Проверка ссылки Помощь с помощью скроллинга страницы')
def test_help_test(browser):
    BasePage(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scrollToitem(HelpPageLocators.ADVERTISEMENT_CABINET)
