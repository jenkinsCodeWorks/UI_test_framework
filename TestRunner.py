import names
from random import randint
from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from prod.pages.CartPage import CartPage
from pages.CheckoutStepOnePage import CheckoutStepOnePage
from pages.CheckoutStepTwoPage import CheckoutStepTwoPage
from pages.CheckoutCompletePage import CheckoutCompletePage


def test_login_and_order(driver_init):
    base_page = BasePage(driver_init)
    login_page = LoginPage(driver_init)
    inventory_page = InventoryPage(driver_init)
    cart_page = CartPage(driver_init)
    checkout_step_one_page = CheckoutStepOnePage(driver_init)
    checkout_step_two_page = CheckoutStepTwoPage(driver_init)
    checkout_complete_page = CheckoutCompletePage(driver_init)

    login_page.go_to()

    assert login_page.get_url() == base_page.base_url, \
        f"Wrong page url: {login_page.get_url()}"
    login_page.make_screenshot()
    login_page.login("standard_user", "secret_sauce")

    assert inventory_page.get_url() == base_page.base_url+"inventory.html", \
        f"Wrong page url: {inventory_page.get_url()}"
    inventory_page.add_to_cart_first_item()
    inventory_page.add_to_cart_first_item()
    inventory_page.add_to_cart_first_item()
    inventory_page.make_screenshot()
    inventory_page.click_on_cart()

    assert cart_page.get_url() == base_page.base_url+"cart.html", f"Wrong page url: {cart_page.get_url()}"
    cart_page.make_screenshot()
    cart_page.click_checkout()

    assert checkout_step_one_page.get_url() == base_page.base_url+"checkout-step-one.html", \
        f"Wrong page url: {checkout_step_one_page.get_url()}"
    checkout_step_one_page.enter_personal_info(names.get_first_name(), names.get_last_name(), randint(100000, 999999))
    checkout_step_one_page.make_screenshot()
    checkout_step_one_page.click_continue()

    assert checkout_step_two_page.get_url() == base_page.base_url+"checkout-step-two.html", \
        f"Wrong page url: {checkout_step_two_page.get_url()}"
    checkout_step_two_page.make_screenshot()
    checkout_step_two_page.click_finish()

    assert checkout_complete_page.get_url() == base_page.base_url+"checkout-complete.html", \
        f"Wrong page url: {checkout_complete_page.get_url()}"
    checkout_complete_page.make_screenshot()
    checkout_complete_page.click_checkout()