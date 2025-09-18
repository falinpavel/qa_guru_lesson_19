from selene import browser
from appium.webdriver.common.appiumby import AppiumBy
from allure import step


class OnboardingPage:
    def __init__(self):
        self.skip_buttom = (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")
        self.continue_button = (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
        self.get_started_button = (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_done_button")

    @step('Tap next button on welcome screen')
    def tap_skip_button_on_welcome_screen(self):
        with step('Tap on the next button on the welcome screen and go to home page'):
            browser.element(self.skip_buttom).click()
        return self

    @step('Tap continue button on welcome screen')
    def tap_continue_button_on_welcome_screen(self):
        with step('Tap on the continue button on the welcome screen and go to home page'):
            browser.element(self.continue_button).click()
        return self

    @step('Skipped welcome screen')
    def tap_continue_button_until_the_get_started_button_appears(self):
        with step('Tap on the continue button and after tap on the get started button'):
            for _ in range(3):
                browser.element(self.continue_button).click()
            browser.element(self.get_started_button).click()