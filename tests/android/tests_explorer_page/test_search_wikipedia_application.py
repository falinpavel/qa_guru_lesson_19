import pytest

from helpers.application_manager.application_manager import wiki_app


class TestSearchWikipediaApplication:
    @pytest.mark.parametrize('search_text', ["Appium", "Bilbo Baggins", "Frodo Baggins"])
    def test_search_wikipedia_application(self, search_text):
        wiki_app.onboarding_page.tap_skip_button_on_welcome_screen()
        wiki_app.home_page \
            .click_search_button_on_wikipedia_home_page() \
            .type_search_text_and_check_result(search_text=search_text) \
            .click_first_article()
