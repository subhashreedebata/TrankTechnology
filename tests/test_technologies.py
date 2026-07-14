import pytest

from pages.technologiespage import technologiespage


@pytest.mark.smoke
def test_technologies_ecomdev_clicking(page):
    ecomdev = technologiespage(page)
    ecomdev.ecomdev_submenus_clicking()

@pytest.mark.smoke
def test_technologies_mobileaappdev_submenus_clicking(page):
    mobileappdev = technologiespage(page)
    mobileappdev.mobile_app_submenus_clicking()