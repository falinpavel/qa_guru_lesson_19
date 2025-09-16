import pytest
import allure
import allure_commons
import os

from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from selene import browser, support
from selenium import webdriver

import const

load_dotenv()

@pytest.fixture(scope='function', autouse=True)
def mobile_management():

    appium_options = UiAutomator2Options().load_capabilities({
        "appium:app": f"{const.APPLICATION_DIR}/app-alpha-universal-release.apk",
        "appium:appWaitActivity": "org.wikipedia.*"
    })

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            command_executor=os.getenv("BS_EXECUTOR"),
            options=appium_options
        )

    browser.config.timeout = float(
        os.getenv('TIMEOUT', '10.0')
    )

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
