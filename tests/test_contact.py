import pytest

from pages.contactpage import contactpage

@pytest.mark.smoke
def test_contact_clicking(page):
    contact = contactpage(page)
    contact.contact_clicking()