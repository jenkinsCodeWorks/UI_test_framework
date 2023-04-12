from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class InventoryPageLocators:
    ADD_TO_CART_BUTTON = (By.XPATH, f"(//*[@class='inventory_item']"
                                    f"//button[text()='Add to cart'])")
    SHOPPING_CART = (By.ID, "shopping_cart_container")


class InventoryPage(BasePage):

    def add_to_cart_first_item(self):
        self.find_element(InventoryPageLocators.ADD_TO_CART_BUTTON).click()

    def click_on_cart(self):
        self.find_element(InventoryPageLocators.SHOPPING_CART).click()
