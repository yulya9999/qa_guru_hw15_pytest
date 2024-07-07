import pytest
from selene import browser, be


desktop_only = pytest.mark.parametrize(
    'browser_screen_resolution', ['1920x1080', '1366x768', '1536x864', '1280x1024'], indirect=True
)

mobile_only = pytest.mark.parametrize(
    "browser_screen_resolution", ['414x896', '390x844', '393x852'], indirect=True
)


@desktop_only
def test_github_desktop(browser_screen_resolution):
    browser.open("https://github.com")
    browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()


@mobile_only
def test_github_mobile(browser_screen_resolution):
    browser.open("https://github.com")
    browser.element('[aria-label="Toggle navigation"].Button--link ').click()
    browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()