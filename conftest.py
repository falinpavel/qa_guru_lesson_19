import pytest
import allure_commons
import os

from allure_commons._allure import step
from appium import webdriver as appium_webdriver
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from selene import browser, support

from const import APK_FILE_PATH
from utils import allure_attachments

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

    with step('init application session'):
        browser.config.driver = appium_webdriver.Remote(
            command_executor=os.getenv("EXECUTOR"),
            options=options
        )

    browser.config.timeout = float(os.getenv('TIMEOUT', '10.0'))

    yield

    allure_attachments.attach_screenshot()
    allure_attachments.attach_xml_dump()

    session_id = browser.driver.session_id

    with step('close application session'):
        browser.quit()

    allure_attachments.attach_bstack_video(session_id)