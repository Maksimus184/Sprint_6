from selenium.webdriver.common.by import By

class DzenPageLocators:
    LOGO_SCOOTER = By.XPATH, '//*[contains(@class, "Header_LogoScooter")]'
    LOGO_DZEN = By.XPATH, '//*[contains(@class, "Header_LogoYandex")]'
    MAIN_PAGE_TITLE = By.XPATH, '//*[contains(@class, "Home_Header")]'
    DZEN_MAIN_PAGE_LOGO = By.XPATH, '//*[contains(@class, "header__logoLink")]'