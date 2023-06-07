
from selene import browser, be, have

browser.config.driver_name = 'chrome'

def test_for_searching_positive(size_window):
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_for_searching_negative(size_window):
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('ysdf/dsf/qqq/we').press_enter()
    browser.element('[id="result-stats"]').should(have.text('About 0 results'))
