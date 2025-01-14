import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.basepage import BasePage
from pageobjects.bc_wallet.onboardingtakecontrol import OnboardingTakeControlPage
from pageobjects.bc_wallet.termsandconditions import TermsAndConditionsPage
#from pageobjects.bc_wallet.onboardingstorecredssecurely import OnboardingStoreCredsSecurelyPage

# These classes can inherit from a BasePage to do common setup and functions
class OnboardingShareNecessaryPage(BasePage):
    """Onboarding Share only what is Necessary Screen page object"""

    # Locators
    # TODO: If Ontario/BC or other wallets are closely alligned and only locators are different, 
    # we could create a locator module that has all the locators. Given a specific app we could load the locators for that app. 
    # not sure this would be a use case that would be common. Leaving locators with the page objects for now.
    on_this_page_text_locator = "Share only what is necessary"
    page_text_locator = "Page Text"
    skip_locator = "Skip"
    back_locator = "com.ariesbifold:id/Back"
    next_locator = "com.ariesbifold:id/Next"

    def on_this_page(self):     
        return super().on_this_page(self.on_this_page_text_locator)

    def get_onboarding_text(self):
        if self.on_this_page():
            pass
        else:
            raise Exception(f"App not on the {type(self)} page")

    def select_next(self):
        if self.on_this_page():
            self.find_by_element_id(self.next_locator).click()
            return OnboardingTakeControlPage(self.driver)
        else:
            raise Exception(f"App not on the {type(self)} page")

    def select_back(self):
        if self.on_this_page():
            self.find_by_element_id(self.back_locator).click()
            from pageobjects.bc_wallet.onboardingstorecredssecurely import OnboardingStoreCredsSecurelyPage
            return OnboardingStoreCredsSecurelyPage(self.driver)
        else:
            raise Exception(f"App not on the {type(self)} page")

    def select_skip(self):
        if self.on_this_page():
            self.find_by_accessibility_id(self.skip_locator).click()
            return TermsAndConditionsPage(self.driver)
        else:
            raise Exception(f"App not on the {type(self)} page")