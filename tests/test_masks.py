from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    """Тестируем функцию get_mask_card_number,
       данные разного формата и пустая строка на вход"""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number(7000792289606361) == "7000 79** **** 6361"
    assert get_mask_card_number("792289606361") == "7922 89** **** "
    assert get_mask_card_number("") == ""


def test_get_mask_account() -> None:
    """Тестируем функцию get_mask_account,
       данные разного формата и пустая строка на вход"""
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account(73654108430135874305) == "**4305"
    assert get_mask_account("736541084") == "**1084"
    assert get_mask_account("") == ""
