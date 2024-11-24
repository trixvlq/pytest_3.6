import time

def test_add_to_cart_button_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    time.sleep(30)

    add_to_cart_button = browser.find_element("css selector", ".btn-add-to-basket")
    assert add_to_cart_button.is_displayed(), "Кнопка добавления в корзину отсутствует!"
