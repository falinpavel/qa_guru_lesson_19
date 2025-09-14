import pytest
import os

from appium.options.android import UiAutomator2Options
from selene import browser
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()

@pytest.fixture(
    scope='function',
    autouse=True
)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        "app": "bs://sample.app",

        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            "userName": os.getenv("BS_LOGIN"),
            "accessKey": os.getenv("BS_PASSWORD"),
        }
    })

    browser.config.driver = webdriver.Remote(
        command_executor="http://hub.browserstack.com/wd/hub",
        options=options
    )

    browser.config.timeout = float(
        os.getenv('timeout', '10.0')
    )

    yield

    browser.quit()