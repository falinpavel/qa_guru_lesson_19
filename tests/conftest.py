import pytest
import allure
import allure_commons
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from dotenv import load_dotenv
from selene import browser, support
from selenium import webdriver
import os

load_dotenv()

def pytest_addoption(parser):
    parser.addoption(
        "--platform", action="store", default="android",
        help="Mobile platform: android or ios"
    )

@pytest.fixture(scope='function', autouse=True)
def mobile_management(request):
    platform = request.config.getoption("platform").lower()

    session_id = browser.driver.session_id

    if platform == 'android':
        options = UiAutomator2Options().load_capabilities({
            "platformName": "Android",
            "platformVersion": "9.0",
            "deviceName": "Google Pixel 3",
            "app": os.getenv("BS_APP_PATH"),

            'bstack:options': {
                "projectName": "wiki",
                "buildName": "browserstack-build-android",
                "sessionName": f"{session_id}-android",
                "userName": os.getenv("BS_LOGIN"),
                "accessKey": os.getenv("BS_PASSWORD"),
            }
        })
    elif platform == 'ios':
        options = XCUITestOptions().load_capabilities({
            "platformName": "iOS",
            "platformVersion": "15.0",
            "deviceName": "iPhone 13 Pro",
            "app": os.getenv("BS_APP_PATH"),

            'bstack:options': {
                "projectName": "wiki",
                "buildName": "browserstack-build-ios",
                "sessionName": f"{session_id}-ios",
                "userName": os.getenv("BS_LOGIN"),
                "accessKey": os.getenv("BS_PASSWORD"),
            }
        })
    else:
        raise ValueError(f"Unsupported platform: {platform}")

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            command_executor=os.getenv("BS_EXECUTOR"),
            options=options
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
