import pytest
import allure_commons
import os

from allure_commons._allure import step
from appium import webdriver as appium_webdriver
from dotenv import load_dotenv
from selene import browser, support

from config import options_management
from utils import allure_attachments


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="bstack_device",
        choices=["bstack_device", "connected_device", "emulator_device"],
        help="Choose device"
    )


def pytest_configure(config):
    context = config.getoption("--context")
    env_file_path = f"env/.env.{context}"

    load_dotenv(dotenv_path=env_file_path)


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function', autouse=True)
def mobile_management(context):
    appium_options = options_management(context=context)

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    with step('init application session'):
        browser.config.driver = appium_webdriver.Remote(
            command_executor=appium_options.get_capability(name="EXECUTABLE_PATH"),
            options=appium_options
        )

    browser.config.timeout = float(os.getenv('TIMEOUT', '10.0'))

    yield

    allure_attachments.attach_screenshot()
    allure_attachments.attach_xml_dump()

    session_id = browser.driver.session_id

    with step('close application session'):
        browser.quit()

    allure_attachments.attach_bstack_video(session_id) if context == "bstack_device" else None