from selene import browser, be


def test_github_desktop(desktop_screen_resolution):
    browser.open("https://github.com")
    browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()


def test_github_mobile(mobile_screen_resolution):
    browser.open("https://github.com")
    browser.element('[aria-label="Toggle navigation"].Button--link ').click()
    browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()