import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    assert len(browser.find_elements_by_id("add_to_basket_form")) >0, \
        'Кнопка добавления товара в корзину отсутсвует'
