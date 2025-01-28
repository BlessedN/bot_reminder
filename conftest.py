import time


import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


@pytest.fixture()
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    yield BasePage(driver)
    driver.quit()


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def xpath(self, locator):
        try:
            received_element = self.driver.find_element(
                by=By.XPATH, value=f'{locator}'
            )
            return True, received_element
        except NoSuchElementException:
            return False, None

    def find_button_and_click(self, locator):
        time.sleep(5)
        received_element = self.xpath(locator)[1]
        if received_element is None:
            return False
        received_element.click()

    def scroll_page(self, locator):
        try:
            action = ActionChains(self.driver)
            received_element = self.xpath(locator)[1]
            action.move_to_element(received_element).perform()
            return True
        except NoSuchElementException:
            return False


