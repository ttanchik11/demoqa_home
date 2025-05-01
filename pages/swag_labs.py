from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage


class SwagLabs(BasePage):
    ICON_LOCATOR = "div.login_logo"
    USERNAME_LOCATOR = "#user-name"
    PASSWORDFIELD_LOCATOR = '#user-name'

    def exist_icon(self):
        try:
            self.find_element(locator="div.login_logo")
        except NoSuchElementException:
            return False
        return True

    def exist_user_name(self):
        try:
            self.find_element(locator='#user-name')
        except NoSuchElementException:
            return False
        return True

    def exist_password_field(self):
        try:
            self.find_element(locator='#password')
        except NoSuchElementException:
            return False
        return True

