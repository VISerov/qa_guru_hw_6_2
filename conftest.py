import pytest

from selene import browser

@pytest.fixture()
def size_window():
    browser.config.driver_name = 'chrome'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
