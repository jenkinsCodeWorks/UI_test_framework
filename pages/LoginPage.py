from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    USER_NAME_BUTTON = (By.ID, "user-name")
    PASSWORD_BUTTON = (By.ID, "password")
    LOGIN_BUTTON_BUTTON = (By.ID, "login-button")


class LoginPage(BasePage):
    def login(self, login, password):
        self.find_element(LoginPageLocators.USER_NAME_BUTTON).send_keys(login)
        self.find_element(LoginPageLocators.PASSWORD_BUTTON).send_keys(password)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_BUTTON).click()

