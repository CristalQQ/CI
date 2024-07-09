import pytest


@pytest.mark.smoke
@pytest.mark.parametrize("page", ["whats_new"], indirect=True)
def test_whats_new(page):
    titel = page.find_element("xpath", "//span[@class='base']").text
    assert titel == "What's New"


@pytest.mark.smoke
@pytest.mark.parametrize("page", ["sale"], indirect=True)
def test_sale(page):
    titel = page.find_element("xpath", "//span[@class='base']").text
    assert titel == "Sale"
