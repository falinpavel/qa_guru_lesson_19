from selene import browser, be
from selene.core.condition import Condition as EC
from appium.webdriver.common.appiumby import AppiumBy
from allure_commons._allure import step


class NavigationBar:
    def __init__(self):
        self.explore_nav_button = (
            AppiumBy.XPATH,
            "(//android.widget.ImageView[@resource-id='org.wikipedia.alpha:id/navigation_bar_item_icon_view'])[1]"
        )
        self.saved_nav_button = (
            AppiumBy.XPATH,
            "(//android.widget.ImageView[@resource-id='org.wikipedia.alpha:id/navigation_bar_item_icon_view'])[2]"
        )
        self.search_nav_button = (
            AppiumBy.XPATH,
            "(//android.widget.ImageView[@resource-id='org.wikipedia.alpha:id/navigation_bar_item_icon_view'])[3]"
        )
        self.edits_nav_button = (
            AppiumBy.XPATH,
            "(//android.widget.ImageView[@resource-id='org.wikipedia.alpha:id/navigation_bar_item_icon_view'])[4]"
        )
        self.more_nav_button = (
            AppiumBy.XPATH,
            "(//android.widget.ImageView[@resource-id='org.wikipedia.alpha:id/navigation_bar_item_icon_view'])[5]"
        )

    @step("Tap navigation bar button 'Explore'")
    def tap_to_explore(self):
        with step("Click on the 'Explore' button and check is oppened"):
            browser.element(self.explore_nav_button).click()
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/view_announcement_text")).should(
                EC.by_and(be.visible)
            )
        return self

    @step("Tap navigation bar button 'Saved'")
    def tap_to_saved(self):
        with step("Click on the 'Saved' button and check is oppened"):
            browser.element(self.saved_nav_button).click()
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Saved")).should(
                EC.by_and(be.visible)
            )
        return self

    @step("Tap navigation bar button 'Search'")
    def tap_to_search(self):
        with step("Click on the 'Search' button and check is oppened"):
            browser.element(self.search_nav_button).click()
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Search")).should(
                EC.by_and(be.visible)
            )
        return self

    @step("Tap navigation bar button 'Edits'")
    def tap_to_edits(self):
        with step("Click on the 'Edits' button and check is oppened"):
            browser.element(self.edits_nav_button).click()
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Edits")).should(
                EC.by_and(be.visible)
            )
        return self

    @step("Tap navigation bar button 'More")
    def tap_to_more(self):
        with step("Click on the 'More' button and check is oppened layout"):
            browser.element(self.more_nav_button).click()
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/main_drawer_account_container")).should(be.visible)
        return self
