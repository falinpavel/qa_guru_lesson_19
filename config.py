import os

import pytest
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options

import utils

load_dotenv(dotenv_path=os.path.expanduser('.'))

from const import APK_FILE_PATH


def options_management(context):
    options = UiAutomator2Options()

    if context == 'emulatora_device':
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.app = APK_FILE_PATH
        options.app_wait_activity = "org.wikipedia.*"
        options.new_command_timeout = 300
        options.connect_hardware_keyboard = True

    if context == 'connected_device':
        # TODO! dont work`t
        pytest.mark.xfail(reason="Real devices not supported")

    if context == 'bstack_device':
        pytest.mark.xfail(reason="bstack does not support")
        # TODO! dont work`t

    return options