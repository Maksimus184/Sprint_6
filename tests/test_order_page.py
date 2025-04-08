import allure
import pytest

from conftest import driver
from data import comment, URLs
from helpers import client_info, about_scooter_rent
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:
    @allure.step('Проверка оформления заказа с валидными данными')
    @pytest.mark.parametrize('button',
                             [MainPageLocators.LOWER_ORDER_BUTTON,
                              MainPageLocators.UPPER_ORDER_BUTTON],
                             )
    def test_create_order(self, driver, button):
        main_page = MainPage(driver)
        driver.get(URLs.MAIN_URL)
        main_page.accept_cookie()
        main_page.create_order(button)
        order_page = OrderPage(driver)
        order_page.fill_form_about_client(
            name=client_info['name'],
            last_name=client_info['last_name'],
            address=client_info['address'],
            metro=client_info['metro'],
            phone=client_info['phone']
        )
        order_page.fill_form_about_rent(
            rent_day=about_scooter_rent['rent_day'],
            colour=about_scooter_rent['colour'],
            comment=comment
        )
        order_page.click_button_order_final()
        order_page.confirmation_order()
        assert 'Заказ оформлен' in order_page.check_accept_order()