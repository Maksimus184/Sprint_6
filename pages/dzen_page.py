import allure

from locators.dzen_page_locators import DzenPageLocators
from pages.base_page import BasePage


class DzenPage(BasePage):
    @allure.step('Переход на главную страницу')
    def go_to_scooter_page(self):
        self.click_to_element(DzenPageLocators.LOGO_SCOOTER)

    @allure.step('Переход на страницу Дзена')
    def go_to_dzen_page(self):
        self.click_to_element(DzenPageLocators.LOGO_DZEN)
        self.switch_window()

    @allure.step('Получение текста заголовка главной страницы')
    def get_scooter_headline_text(self):
        return self.get_text_from_element(DzenPageLocators.MAIN_PAGE_TITLE)

    @allure.step('Найти логотип на странице Дзена')
    def check_dzen_button(self):
        return self.find_element_with_wait(DzenPageLocators.DZEN_MAIN_PAGE_LOGO)