import pytest
import allure
import allure_commons
import os

from allure_commons._allure import step
from appium import webdriver as appium_webdriver
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from selene import browser, support

from const import APK_FILE_PATH

load_dotenv()

@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.app = APK_FILE_PATH
    options.app_wait_activity = "org.wikipedia.*"
    options.new_command_timeout = 300
    options.connect_hardware_keyboard = True

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    with step('init app session'):
        browser.config.driver = appium_webdriver.Remote(
            command_executor=os.getenv("EXECUTOR"),
            options=options
        )

    browser.config.timeout = float(os.getenv('TIMEOUT', '10.0'))

    yield

    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
    )

    allure.attach(
        browser.driver.page_source,
        name='screen xml dump',
        attachment_type=allure.attachment_type.XML,
    )

    browser.quit()
