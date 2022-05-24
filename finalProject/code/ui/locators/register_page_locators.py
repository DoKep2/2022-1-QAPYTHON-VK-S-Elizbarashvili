from selenium.webdriver.common.by import By


class RegisterPageLocators:
    NAME_INPUT = (By.CSS_SELECTOR, "#user_name")
    SURNAME_INPUT = (By.CSS_SELECTOR, "#user_surname")
    MIDDLE_NAME_INPUT = (By.CSS_SELECTOR, "#user_middle_name")
    USERNAME_INPUT = (By.CSS_SELECTOR, "#username")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#confirm")
    CONFIRM_CHECKBOX = (By.CSS_SELECTOR, "#term")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
