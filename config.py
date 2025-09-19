import os
import pytest

from appium.options.android import UiAutomator2Options

from const import APK_FILE_PATH


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
        # TODO! dont work`t
        pytest.mark.xfail(reason="bstack does not support")
        options.set_capability(
            name="EXECUTABLE_PATH",
            value=os.getenv("EXECUTABLE_PATH")
        )

    return options
