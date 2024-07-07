import pytest
from selene import browser


@pytest.fixture(params=['1920x1080', '1366x768', '1536x864', '1280x1024'])
def desktop_screen_resolution(request):
    width, height = map(int, request.param.split('x'))
    browser.config.window_width = width
    browser.config.window_height = height

    yield
    browser.quit()


@pytest.fixture(params=['414x896', '390x844', '393x852'])
def mobile_screen_resolution(request):
    width, height = map(int, request.param.split('x'))
    browser.config.window_width = width
    browser.config.window_height = height

    yield
    browser.quit()


@pytest.fixture(params=['1920x1080', '1366x768', '1536x864', '1280x1024', '414x896', '390x844', '393x852'])
def browser_screen_resolution(request):
    width, height = map(int, request.param.split('x'))
    browser.config.window_width = width
    browser.config.window_height = height

    yield
    browser.quit()


@pytest.fixture(params=['1920x1080', '1366x768', '1536x864', '1280x1024', '414x896', '390x844', '393x852'])
def screen_resolution(request):
    width, height = map(int, request.param.split("x"))
    browser.config.window_width = width
    browser.config.window_height = height
    if request.param in ['1920x1080', '1366x768', '1536x864', '1280x1024']:
        yield "desktop"
    else:
        yield "mobile"

    browser.quit()
