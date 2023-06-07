import pytest

from selene import browser
browser.config.driver_name = 'chrome'
@pytest.fixture()
def size_window():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
