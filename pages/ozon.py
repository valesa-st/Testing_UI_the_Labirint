import os
import pickle
from pages.base import WebPage
from pages.elements import WebElement


class OzonPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.ozon.ru/'
        super().__init__(web_driver, url)

    LOCATOR_CONTACT = WebElement(xpath='//a[@title="Контакты"]')
    LOCATOR_SEARCH_BAR = WebElement(xpath='//input[@placeholder="Искать на Ozon"]')
    LOCATOR_SEARCH_BAR_BTN = WebElement(class_name='aa3f')
    LOCATOR_FILTER_BAR = WebElement(class_name='ui-t5')
    LOCATOR_ELECTRONICA = WebElement(xpath='//*[@id="layoutPage"]/div[1]/header/div[2]/div/ul/li[10]/a')
