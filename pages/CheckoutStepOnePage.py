from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class CheckoutStepOnePageLocators:
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

class CheckoutStepOnePage(BasePage):
    def enter_personal_info(self, first_name="", last_name="", postal_code=""):
        self.find_element(CheckoutStepOnePageLocators.FIRST_NAME_INPUT).send_keys(first_name)
        self.find_element(CheckoutStepOnePageLocators.LAST_NAME_INPUT).send_keys(last_name)
        self.find_element(CheckoutStepOnePageLocators.POSTAL_CODE_INPUT).send_keys(postal_code)

    def click_continue(self):
        self.find_element(CheckoutStepOnePageLocators.CONTINUE_BUTTON).click()