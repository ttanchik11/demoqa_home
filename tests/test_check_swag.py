#ДЗ №6

from pages.swag_labs import SwagLabs

def test_check_swag_icon(browser):
    swag_page = SwagLabs(browser)
    swag_page.visit()
    assert swag_page.exist_icon(), "Иконка не найдена на странице"

def test_check_user_name(browser):
    swag_page = SwagLabs(browser)
    swag_page.visit()
    assert swag_page.exist_user_name(), "Поле не найдено на странице"

def test_check_password_field(browser):
    swag_page = SwagLabs(browser)
    swag_page.visit()
    assert swag_page.exist_password_field(), "Поле не найдено на странице"
