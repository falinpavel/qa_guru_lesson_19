import pytest

from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@pytest.mark.parametrize(
    "to_search",
    ["Appium"]
)
def test_search_and_check_result_list(to_search):
    with step(f'Tap on search field and type request: {to_search}'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(to_search)
    with step(f'Verify content found, check that {to_search} is present'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text(to_search))


@pytest.mark.parametrize(
    "to_search",
    ["Bilbo Baggins", "Frodo Baggins"]
)
def test_search_and_go_to_article_page(to_search):
    with step(f'Tap on search field and type request: {to_search}'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(to_search)
    with step(f'Check that {to_search} is present and go to article page'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
    with step(f'Verify content found, check that {to_search} is present and go to article page'):
        results.first.should(have.text(to_search)).click()
