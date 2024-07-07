import pytest
from selene import browser, be


def test_github_desktop(screen_resolution):
    if screen_resolution == "mobile":
        pytest.skip(reason="skip the mobile test")

    browser.open("https://github.com")
    browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()


def test_github_mobile(screen_resolution):
    if screen_resolution == "desktop":
        pytest.skip(reason="skip the desktop test")

    browser.open("https://github.com")
    browser.element('[aria-label="Toggle navigation"].Button--link ').click()
    browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()
