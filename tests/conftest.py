import allure_commons
import pytest
import os

from appium.options.android import UiAutomator2Options
from selene import browser, support
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()

@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        "app": os.getenv("BS_APP_PATH"),

        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            "userName": os.getenv("BS_LOGIN"),
            "accessKey": os.getenv("BS_PASSWORD"),
        }
    })

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    browser.config.driver = webdriver.Remote(
        command_executor=os.getenv("BS_EXECUTOR"),
        options=options
    )

    browser.config.timeout = float(
        os.getenv('TIMEOUT', '10.0')
    )

    yield

    browser.quit()