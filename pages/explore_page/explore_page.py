from selene import browser, have
from appium.webdriver.common.appiumby import AppiumBy
from allure_commons._allure import step


class ExplorePage:
    def __init__(self):
        self.search_field_button = (AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")
        self.search_src_field = (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")
        self.list_all_results = (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')

    @step('Tap to search button on wikipedia home page')
    def click_search_button_on_wikipedia_home_page(self):
        with step('Click on the search button on the wikipedia home page'):
            browser.element(self.search_field_button).click()
        return self

    @step('Tap fie')
    def type_search_text_and_check_result(self, search_text):
        with step(f'Typing {search_text} in search field'):
            browser.element(self.search_src_field).type(search_text)
            results = browser.all(self.list_all_results)
            results.should(have.size_greater_than(0))
            results.first.should(have.text(search_text))
        return self

    @step('Click on article on result list')
    def click_first_article(self):
        with step('Click on article on result list'):
            results = browser.all(self.list_all_results)
            results.first.click()
        return self
