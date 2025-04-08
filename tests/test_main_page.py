import allure
import pytest

from data import answer_for_question, URLs
from conftest import driver
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage


class TestsMainPage:
    # Проверка выпадающего списка FAQ
    @allure.title('Проверка выпадающего списка вопросы-ответы')
    @pytest.mark.parametrize("question_id, expected_answer", answer_for_question.items())
    def test_check_answer_for_question(self, driver, question_id, expected_answer):
        main_page = MainPage(driver)
        driver.get(URLs.MAIN_URL)
        main_page.accept_cookie()
        # Теперь вызываем метод и проверяем ответ
        actual_answer = main_page.check_answer_for_question(question_id)
        # Проверяем, соответствует ли фактический ответ ожидаемому
        assert actual_answer == expected_answer


    # проверка корректности работы верхней кнопки Заказать
    @allure.title('Проверка верхней кнопки Заказать')
    def test_click_order_button_up(self, driver):
        main_page = MainPage(driver)
        driver.get(URLs.MAIN_URL)
        main_page.accept_cookie()
        main_page.upper_order_button_click()
        assert main_page.find_element_with_wait(OrderPageLocators.ORDER_PAGE_TITLE)

    # проверка работы нижней кнопки Заказать
    @allure.title('Проверка нижней кнопки Заказать')
    def test_click_order_button_down(self,driver):
        main_page = MainPage(driver)
        driver.get(URLs.MAIN_URL)
        main_page.accept_cookie()
        main_page.scroll_for_order_button_down()
        main_page.lower_order_button_click()
        assert main_page.find_element_with_wait(OrderPageLocators.ORDER_PAGE_TITLE)