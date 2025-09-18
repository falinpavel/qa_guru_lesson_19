from components.navigation_bar.navigation_bar import NavigationBar
from pages.explore_page.explore_page import ExplorePage
from pages.onboarding_page.onboarding_page import OnboardingPage


class AndroidApplicationManager:
    def __init__(self):
        self.home_page = ExplorePage()
        self.onboarding_page = OnboardingPage()
        self.navigation_bar = NavigationBar()

wiki_app = AndroidApplicationManager()
