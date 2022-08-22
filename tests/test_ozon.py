# python -m pytest -v --driver chrome --driver-path chromedriver.exe tests/test_ozon.py


import time
import pytest
import pickle
from pages.base import WebPage
from pages.ozon import OzonPage


def test_scroll_down_and_contact_click(web_browser):
    page = OzonPage(web_browser)
    page.scroll_down()
    page.LOCATOR_CONTACT.is_visible()
    page.LOCATOR_CONTACT.click()
    assert page.get_current_url() == 'https://docs.ozon.ru/common/kontakty/'
