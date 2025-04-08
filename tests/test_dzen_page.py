import allure

from data import URLs
from pages.main_page import MainPage
from pages.dzen_page import DzenPage
from conftest import driver


class TestSwitchPage:
    @allure.title('Проверка перехода на главную страницу по клику на лого Самоката')
    def test_transition_from_order_page_to_main_page(self, driver,):
        switch_page = DzenPage(driver)
        main_page = MainPage(driver)
        driver.get(URLs.MAIN_URL)
        main_page.accept_cookie()
        main_page.upper_order_button_click()
        switch_page.go_to_scooter_page()
        assert 'Самокат' in switch_page.get_scooter_headline_text()

    @allure.title('Проверка перехода на Дзен по клику на лого Дзена')
    def test_transition_from_order_page_to_dzen(self, driver):
        switch_page = DzenPage(driver)
        main_page = MainPage(driver)
        driver.get(URLs.MAIN_URL)
        main_page.accept_cookie()
        switch_page.go_to_dzen_page()
        assert switch_page.check_dzen_button()