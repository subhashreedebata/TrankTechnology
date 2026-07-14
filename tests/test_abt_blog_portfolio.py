import pytest

from pages.abt_blog_portfolio_page import abt_blog_portfolio_page


@pytest.mark.smoke
def test_abp_clicking(page):
    abp = abt_blog_portfolio_page(page)
    abp.abp_clicking()
