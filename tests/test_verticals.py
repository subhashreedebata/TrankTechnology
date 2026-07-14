import pytest

from pages.verticalpage import verticalpage

@pytest.mark.trading
def test_trading_clicking(page):
    trading = verticalpage(page)
    trading.trading_submenus_clicking()

@pytest.mark.trading
def test_retail_clicking(page):
    retail = verticalpage(page)
    retail.retail_submenus_clicking()

@pytest.mark.trading
def test_healthcare_clicking(page):
    healthcare = verticalpage(page)
    healthcare.healthcare_submenus_clicking()

@pytest.mark.smoke
def test_fintech_clicking(page):
    fintech = verticalpage(page)
    fintech.fintech_submenus_clicking()

@pytest.mark.smoke
def test_customapp_clicking(page):
    customapp = verticalpage(page)
    customapp.customapp_submenus_clicking()