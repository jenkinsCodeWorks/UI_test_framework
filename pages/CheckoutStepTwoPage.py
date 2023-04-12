from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class CheckoutStepTwoPageLocators:
    FINISH_BUTTON = (By.ID, "finish")


class CheckoutStepTwoPage(BasePage):
    def click_finish(self):
        self.find_element(CheckoutStepTwoPageLocators.FINISH_BUTTON).click()
