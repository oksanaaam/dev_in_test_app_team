import pytest
from appium import webdriver
from framework.login_page import LoginPage


@pytest.fixture(scope="module")
def driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "Pixel 5 API 33",
        "appPackage": "com.ajaxsystems",
        "appActivity": "com.ajaxsystems.ui.activity.LauncherActivity"
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login_page(driver):
    page = LoginPage(driver)
    page.open_login_page()
    yield page


@pytest.mark.parametrize("username, password, result", [
    ("qa.ajax.app.automation@gmail.com", "qa_automation_password", True),
    ("invalid_user", "qa_automation_password", False),
    ("qa.ajax.app.automation@gmail.com", "invalid_password", False)
])
def test_login(login_page, username, password, result):
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()
    assert login_page(username, password) == result
