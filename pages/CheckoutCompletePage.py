from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class CheckoutCompletePageLocators:
    BACK_TO_PRODUCTS = (By.ID, "back-to-products")

class CheckoutCompletePage(BasePage):
    def click_checkout(self):
        self.find_element(CheckoutCompletePageLocators.BACK_TO_PRODUCTS).click()