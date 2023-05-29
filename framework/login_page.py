from appium.webdriver.common.mobileby import MobileBy

from .page import Page


class LoginPage(Page):
    USERNAME_INPUT = (MobileBy.ID, 'username')
    PASSWORD_INPUT = (MobileBy.ID, 'password')
    LOGIN_BUTTON = (MobileBy.ID, 'login-button')

    def enter_username(self, username):
        username_input = self.find_element(self.USERNAME_INPUT)
        username_input.clear()
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.find_element(self.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
