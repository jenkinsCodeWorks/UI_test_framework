import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# @pytest.fixture(scope="module", params=["chrome", "edge", "firefox"])
# def driver_init(request):
#     if request.param == "chrome":
#         capabilities = DesiredCapabilities.CHROME.copy()
#     elif request.param == "edge":
#         capabilities = DesiredCapabilities.EDGE.copy()
#     elif request.param == "firefox":
#         capabilities = DesiredCapabilities.FIREFOX.copy()
#     else:
#         raise ValueError("Invalid browser name")
#     driver = webdriver.Remote(
#         command_executor="http://127.0.0.1:4444/wd/hub",
#         desired_capabilities=capabilities,
#     )
#     yield driver
#     driver.quit()


# for localHost launch
# @pytest.fixture(scope="module")
# def driver_init():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()