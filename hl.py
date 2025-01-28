import time

import allure
from allure_commons.types import LabelType, AttachmentType


@allure.id("2")
@allure.title('Тест "Nice-case"')
@allure.feature('Автоматизированный тест - "Nice-case"')
@allure.tag('UI')
@allure.severity('trivial')
@allure.label(LabelType.FRAMEWORK, "pytest")
def test_nice_case(browser):
    browser.open_url('https://nice-case.ru/catalog/apple/')

    with allure.step('Переход к нужным товарам'):
        browser.xpath(locator='//*[@id="bx_1847241719_395"]')
        browser.find_button_and_click(locator='//*[@id="bx_1847241719_395"]')
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="Screenshot",
            attachment_type=AttachmentType.PNG
        )

    with allure.step('Выбираем в чек-боксе нужные фильтры №1 (Указываем модель)'):
        if browser.scroll_page(
                '//span[@class="bx_filter_param_text" '
                'and @title="iPhone 16 Pro Max"]'
        ):
            browser.xpath(
                '//span[@class="bx_filter_param_text" '
                'and @title="iPhone 16 Pro Max"]')
            browser.find_button_and_click(
                '//span[@class="bx_filter_param_text" '
                'and @title="iPhone 16 Pro Max"]'
            )
        else:
            assert False, "Элемент не найден при скроллинге."
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="Screenshot",
            attachment_type=AttachmentType.PNG
        )

    with allure.step('Выбираем в чек-боксе нужные фильтры №2 (Указываем количетсво памяти)'):
        if browser.scroll_page(
                '//span[@class="bx_filter_param_text" and @title="512GB"]'):
            browser.xpath(
                '//span[@class="bx_filter_param_text" and @title="512GB"]')
            browser.find_button_and_click(
                 '//span[@class="bx_filter_param_text" and @title="512GB"]'
            )
        else:
            assert False, "Элемент не найден при скроллинге."
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="Screenshot",
            attachment_type=AttachmentType.PNG
        )

    with allure.step('Выбираем нужную модель телефона'):
        if browser.scroll_page(
                '//*[@id="bx_3966226736_146562"]'):
            browser.xpath(
                '//*[@id="bx_3966226736_146562"]')
            browser.find_button_and_click(
                 '//*[@id="bx_3966226736_146562"]'
            )
        else:
            assert False, "Элемент не найден при скроллинге."
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="Screenshot",
            attachment_type=AttachmentType.PNG
        )

    with allure.step('Добавление телефона в корзину'):
        if browser.scroll_page(
                '//*[starts-with(@id, "bx_117848907") and'
                ' @class="button_block wide"]'):
            time.sleep(2)
            browser.xpath(
                '//*[starts-with(@id, "bx_117848907") and'
                ' @class="button_block wide"]')
            browser.find_button_and_click(
                 '//*[starts-with(@id, "bx_117848907") and'
                 ' @class="button_block wide"]'
            )
        else:
            assert False, "Элемент не найден при скроллинге."
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="Screenshot",
            attachment_type=AttachmentType.PNG
        )

    with allure.step('Переход в корзину'):
        if browser.scroll_page(
                '//*[starts-with(@id, "bx_117848907") and @class="button_block wide"]'):
            time.sleep(3)
            browser.xpath(
                '//*[starts-with(@id, "bx_117848907") and'
                ' @class="button_block wide"]')
            time.sleep(2)
            browser.find_button_and_click(
                 '//*[starts-with(@id, "bx_117848907") and'
                 ' @class="button_block wide"]'
            )
        else:
            assert False, "Элемент не найден при скроллинге."
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="Screenshot",
            attachment_type=AttachmentType.PNG
        )
