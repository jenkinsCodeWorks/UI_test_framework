from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class CartPageLocators:
    CHECKOUT_BUTTON = (By.ID, "checkout")

class CartPage(BasePage):
    def click_checkout(self):
        self.find_element(CartPageLocators.CHECKOUT_BUTTON).click()