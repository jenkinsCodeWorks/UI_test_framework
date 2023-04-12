import os
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from time import strftime
from random import randint
from a_selenium_screenshot_whole_page import get_screenshot_whole_page_with_scroll


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.saucedemo.com/"
        self.curr_dir = os.getcwd()
        self.screenshots_dir = os.path.join(self.curr_dir, "../screenshots")


    def find_element(self, locator, time=5):
        return wait(self.driver, 5).until(EC.presence_of_element_located(locator),
                                          message=f"There is no such element {locator}")


    def find_many_elements(self, locator, time=5):
        return wait(self.driver, 5).until(EC.presence_of_all_elements_located(locator),
                                          message=f"There are no such elements {locator}")


    def go_to(self):
        return self.driver.get(self.base_url)


    def get_title(self):
        return self.driver.title


    def get_url(self):
        return self.driver.current_url


    def make_screenshot(self):
        screenshot_dir = os.path.join(os.getcwd(), 'screenshots')

        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        filename = strftime('%Y.%m.%d...%H_%M_%S') + f'_{randint(10000, 100000)}.png'
        screenshot_path = os.path.join(screenshot_dir, filename)
        get_screenshot_whole_page_with_scroll(self.driver, sleepinterval=(0.2, 0.8), save_path=screenshot_path)
