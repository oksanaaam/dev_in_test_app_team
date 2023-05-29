import pytest
from selenium import webdriver
from framework.login_page import LoginPage


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login_page(driver):
    page = LoginPage(driver)
    page.driver.get("https://example.com/login")
    yield page


@pytest.mark.parametrize("username, password", [
    ("valid_user", "valid_password"),
    ("invalid_user", "valid_password"),
    ("valid_user", "invalid_password")
])
def test_login(login_page, username, password):
    login_page.login(username, password)
    assert login_page.is_login_successful()
