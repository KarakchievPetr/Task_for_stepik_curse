import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart_button_is_displayed(browser):
    browser.get(link)
    assert len(browser.find_elements_by_id("add_to_basket_form")) >0, \
        'Кнопка добавления товара в корзину отсутсвует'
