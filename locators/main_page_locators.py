from selenium.webdriver.common.by import By

class MainPageLocators:
    UPPER_ORDER_BUTTON = By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[@class="Button_Button__ra12g" and text()="Заказать"]'
    LOWER_ORDER_BUTTON = By.XPATH, '//button[contains(@class, "Button_Middle") and text() = "Заказать"]'
    COOKIE_BUTTON = By.ID, 'rcc-confirm-button'
    QUESTION_LOCATOR = By.XPATH, '//div[@id="accordion__heading-{}"]'
    ANSWER_LOCATOR = By.XPATH, '//div[@id="accordion__panel-{}"]/p'
    SCROLL_TO_QUESTION_LOCATOR = By.XPATH, '//div[@id="accordion__heading-7"]'