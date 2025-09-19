import os
import pytest

from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv

from const import APK_FILE_PATH


def platform_managment(context_platform):
    pass

def options_management(context):
    options = UiAutomator2Options()

    if context == 'emulator_device':
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.app = APK_FILE_PATH
        options.app_wait_activity = "org.wikipedia.*"
        options.new_command_timeout = 300
        options.connect_hardware_keyboard = True
        options.set_capability(name="EXECUTABLE_PATH", value=os.getenv("EXECUTABLE_PATH"))

    if context == 'connected_device':
        # TODO! dont work`t
        pytest.mark.xfail(reason="Real devices not supported")

    if context == 'bstack_device':
        options.platform_name = "Android"
        options.device_name = "Google Pixel 3"
        options.app = os.getenv("BS_APP_PATH")
        options.set_capability(name="EXECUTABLE_PATH", value=os.getenv("EXECUTABLE_PATH"))
        options.set_capability(name="bstack:options", value={
            "projectName": "First Python project", # Название проекта которое будет отображаться в Browserstack
            "buildName": "browserstack-build-1", # Название сборки которое будет отображаться в Browserstack
            "sessionName": "BStack first_test", # Название сессии которое будет отображаться в Browserstack
            # Set your access credentials
            "userName": os.getenv("BS_LOGIN"), # Ваш логин в Browserstack
            "accessKey": os.getenv("BS_PASSWORD") # Ваш ключ доступа в Browserstack
        })

    return options
