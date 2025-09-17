import pytest

from helpers.application_manager.application_manager import wiki_app


class TestSearchWikipediaApplication:
    @pytest.mark.parametrize('search_text', ["Appium", "Bilbo Baggins", "Frodo Baggins"])
    def test_search_wikipedia_application(self, search_text):
        wiki_app.home_page \
            .click_next_button_on_welcome_screen() \
            .click_search_button_on_wikipedia_home_page() \
            .type_search_text_and_check_him_is_present(search_text=search_text) \
            .click_first_article()
