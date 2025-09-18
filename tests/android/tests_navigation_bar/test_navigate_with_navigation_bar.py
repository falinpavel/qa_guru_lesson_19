from helpers.application_manager.application_manager import wiki_app
from tests.android.tests_onboarding_page.test_skipped_welcome_screen import TestSkippedWelcomeScreen


class TestNavigationBar:
    def test_navigate_in_application_with_navigation_bar(self):
        wiki_app.onboarding_page.navigate_with_navigation_bar()
        wiki_app.navigation_bar.tap_to_saved()