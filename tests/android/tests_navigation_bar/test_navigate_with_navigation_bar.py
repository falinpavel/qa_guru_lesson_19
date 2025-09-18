from helpers.application_manager.application_manager import wiki_app


class TestNavigationBar:
    def test_navigate_in_application_with_navigation_bar(self):
        wiki_app.onboarding_page.tap_skip_button_on_welcome_screen()
        wiki_app.navigation_bar \
            .tap_to_explore() \
            .tap_to_saved() \
            .tap_to_search() \
            .tap_to_edits() \
            .tap_to_more()