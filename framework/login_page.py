from .page import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):
    USERNAME_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

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
