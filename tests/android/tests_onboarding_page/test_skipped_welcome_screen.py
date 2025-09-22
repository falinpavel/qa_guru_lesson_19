from helpers.application_manager.application_manager import wiki_app


class TestSkippedWelcomeScreen:
    def test_skipped_welcome_screen_with_tap_skip_button(self):
        wiki_app.onboarding_page.tap_continue_button_until_the_get_started_button_appears()

    def test_skipped_welcome_screen_with_tapping_on_continue(self):
        wiki_app.onboarding_page.tap_skip_button_on_welcome_screen()
