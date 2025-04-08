from selenium.webdriver.common.by import By

class OrderPageLocators:

    # страница ввода информации о заказчике
    ORDER_PAGE_TITLE = By.XPATH, '//div[text()="Для кого самокат"]'
    INPUT_NAME = By.XPATH, '//input[@placeholder="* Имя"]'
    INPUT_SURNAME = By.XPATH, '//input[@placeholder="* Фамилия"]'
    INPUT_ADDRESS = By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'
    INPUT_PHONE = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'
    INPUT_METRO = By.XPATH, '//input[@placeholder = "* Станция метро"]'
    SELECT_STATION = By.XPATH, '//*[contains(@class, "Order_Text") and text()="{}"]'
    BUTTON_NEXT = By.XPATH, '//button[text()="Далее"]'

    # страница ввода информации об аренде
    ORDER_RENT_TITLE = By.XPATH, '//div[text()="Про аренду"]'
    INPUT_RENT_DATE = By.XPATH, '//input[@placeholder = "* Когда привезти самокат"]'
    SELECT_DATE = By.XPATH, '//div[@tabindex="0" and contains(@class, "react-datepicker__day")]'
    INPUT_RENTAL_PERIOD = By.XPATH, '//div[@class="Dropdown-placeholder" and text()="* Срок аренды"]'
    SELECT_RENTAL_PERIOD = By.XPATH, '//div[@class="Dropdown-option" and text()="{}"]'
    COLOUR_CHECKBOX = By.XPATH, '//*[@id="{}"]'
    INPUT_COMMENT = By.XPATH, '//input[@placeholder = "Комментарий для курьера"]'
    BUTTON_BACK = By.XPATH, '//button[text()="Назад"]'
    BUTTON_ORDER = By.XPATH, '//button[contains(@class, "Button_Middle") and text()="Заказать"]'

    # всплывающие окна
    ORDER_CONFIRMATION_TITLE = By.XPATH, '//div[text()="Хотите оформить заказ?"]'
    YES_BUTTON = By.XPATH, '//button[text()="Да"]'
    ORDER_IS_PLACED = By.XPATH, '//div[text()="Заказ оформлен"]'