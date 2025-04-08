import allure

from helpers import generate_date_rent
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполнение поля Имя')
    def fill_in_name(self, name):
        return self.add_text_to_element(OrderPageLocators.INPUT_NAME, name)

    @allure.step('Заполнение поля Фамилия')
    def fill_in_surname(self, last_name):
        return self.add_text_to_element(OrderPageLocators.INPUT_SURNAME, last_name)

    @allure.step('Заполнение поля Адресс')
    def fill_in_address(self, address):
        return self.add_text_to_element(OrderPageLocators.INPUT_ADDRESS, address)

    @allure.step('Заполнение поля Метро')
    def fill_in_metro(self, metro):
        return self.add_text_to_element(OrderPageLocators.INPUT_METRO, metro)

    @allure.step('Выбор станции метро из списка')
    def click_from_element_list_metro(self, metro):
        locator_metro = self.format_locators(OrderPageLocators.SELECT_STATION, metro)
        return self.click_to_element(locator_metro)

    @allure.step('Заполнение поле Телефон')
    def fill_in_phone(self, phone):
        return self.add_text_to_element(OrderPageLocators.INPUT_PHONE, phone)

    @allure.step('Заполнение формы Для кого самокат')
    def fill_form_about_client(self, name, last_name, address, metro, phone):
        self.fill_in_name(name)
        self.fill_in_surname(last_name)
        self.fill_in_address(address)
        self.fill_in_metro(metro)
        self.click_from_element_list_metro(metro)
        self.fill_in_phone(phone)
        self.click_to_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Заполнение поля Когда привезти самокат')
    def fill_in_date_rent(self):
        rent_date = generate_date_rent()
        day = rent_date.split('.')[0]
        self.add_text_to_element(OrderPageLocators.INPUT_RENT_DATE, rent_date)
        day_calendar_locator = self.format_locators(OrderPageLocators.SELECT_DATE, day)
        return self.click_to_element(day_calendar_locator)

    @allure.step('Заполнение поля Срок аренды')
    def fill_in_count_rent_day(self, rent_day):
        self.click_to_element(OrderPageLocators.INPUT_RENTAL_PERIOD)
        locator_count_rent_day = self.format_locators(OrderPageLocators.SELECT_RENTAL_PERIOD, rent_day)
        return self.click_to_element(locator_count_rent_day)


    @allure.step('Выбор чек-бокса')
    def fill_in_checkbox_colour(self, colour):
        scooter_colour = self.format_locators(OrderPageLocators.COLOUR_CHECKBOX, colour)
        return self.click_to_element(scooter_colour)

    @allure.step('Заполнение поля Комментарий')
    def fill_in_comment(self,comment):
        return self.add_text_to_element(OrderPageLocators.INPUT_COMMENT, comment)

    @allure.step('Заполнение формы Про аренду')
    def fill_form_about_rent(self, rent_day, colour, comment):
        self.fill_in_date_rent()
        self.fill_in_count_rent_day(rent_day)
        self.fill_in_checkbox_colour(colour)
        self.fill_in_comment(comment)

    @allure.step('Клик на кнопку Заказать в форме')
    def click_button_order_final(self):
        self.click_to_element(OrderPageLocators.BUTTON_ORDER)

    @allure.step('Подтверждение заказа')
    def confirmation_order(self):
        self.click_to_element(OrderPageLocators.YES_BUTTON)

    @allure.step('Получение подтверждения об оформленном заказе')
    def check_accept_order(self):
        return self.get_text_from_element(OrderPageLocators.ORDER_IS_PLACED)