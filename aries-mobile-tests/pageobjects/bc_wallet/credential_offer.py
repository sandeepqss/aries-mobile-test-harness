import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.basepage import BasePage
from pageobjects.bc_wallet.credential_on_the_way import CredentialOnTheWayPage


# These classes can inherit from a BasePage to do common setup and functions
class CredentialOfferPage(BasePage):
    """Credential Offer Notification page object"""

    # Locators
    on_this_page_text_locator = "is offering you a credential"
    credential_locator = "offer"
    who_locator = "issuer"
    cred_type_locator = "credential type"
    attribute_locator = "attribute"
    value_locator = "value"
    accept_locator = "Accept"
    decline_locator = "Decline"

    def on_this_page(self):
        #print(self.driver.page_source)
        return super().on_this_page(self.on_this_page_text_locator)

    def select_accept(self):
        if self.on_this_page():
            self.find_by_accessibility_id(self.accept_locator).click()
            return CredentialOnTheWayPage(self.driver)
        else:
            raise Exception(f"App not on the {type(self)} page")

    def select_decline(self):
        if self.on_this_page():
            self.find_by_accessibility_id(self.accept_locator).click()
            # Not sure what is returned here yet
            # return CredentialOfferPage(self.driver)
        else:
            raise Exception(f"App not on the {type(self)} page")

    def get_credential_details(self):
        if self.on_this_page():
            who = self.find_by_accessibility_id(self.who_locator).text
            cred_type = self.find_by_accessibility_id(self.cred_type_locator).text
            attribute_elements = self.find_multiple_by_id(self.attribute_locator)
            value_elements = self.find_multiple_by_id(self.values_locator)
            attributes = []
            for attribute in attribute_elements:
                attributes = attributes.append[attribute.text]
            values = []
            for value in value_elements:
                values = values.append[value.text]
            return who, cred_type, attributes, values
        else:
            raise Exception(f"App not on the {type(self)} page")
