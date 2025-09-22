import os

from appium.options.android import UiAutomator2Options

from const import APK_FILE_PATH


def platform_management(context_platform):
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
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.device_name = "RF8N9193HQY"  # samsung s20 fe
        options.app = APK_FILE_PATH
        options.app_wait_activity = "org.wikipedia.*"
        options.new_command_timeout = 300
        options.connect_hardware_keyboard = True
        options.set_capability(name="EXECUTABLE_PATH", value=os.getenv("EXECUTABLE_PATH"))

    if context == 'bstack_device':
        options.platform_name = "Android"
        options.device_name = "Google Pixel 3"
        options.app = os.getenv("BS_APP_PATH")
        options.set_capability(name="EXECUTABLE_PATH", value=os.getenv("EXECUTABLE_PATH"))
        options.set_capability(name="bstack:options", value={
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",
            "userName": os.getenv("BS_LOGIN"),
            "accessKey": os.getenv("BS_PASSWORD")
        })

    return options
