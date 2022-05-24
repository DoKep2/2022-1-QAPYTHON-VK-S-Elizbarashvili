from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_INPUT = (By.CSS_SELECTOR, "#username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#submit")
    CREATE_ACCOUNT_LINK = (By.XPATH, "//a[@href='/reg']")
    INCORRECT_USERNAME_OR_PASSWORD_ALERT = (By.XPATH, "//div[contains(text(), 'Invalid username or password')]")
    INCORRECT_USERNAME_LENGTH_ALERT = (By.XPATH, "//div[contains(text(), 'Incorrect username length')]")
