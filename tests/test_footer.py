import pytest

from pages.footerpage import footerpage


@pytest.mark.smoke
def test_webdevelopement_clicking(page):
    webdev = footerpage(page)
    webdev.webelement_submenus_clicking()

@pytest.mark.smoke
def test_uiux_clicking(page):
    uiux = footerpage(page)
    uiux.uiux_submenus_clicking()

@pytest.mark.smoke
def test_appdevelopement_clicking(page):
    appdev = footerpage(page)
    appdev.appdevelopement_submenus_clicking()

@pytest.mark.smoke
def test_graphics_clicking(page):
    graphics = footerpage(page)
    graphics.graphics_submenus_clicking()

@pytest.mark.smoke
def test_followuslink_clicking(page):
    follow_us = footerpage(page)
    follow_us.followuslink_submenus_clicking()

