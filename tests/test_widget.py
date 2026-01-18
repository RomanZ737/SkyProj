from src.widget import mask_account_card, get_date
import pytest

@pytest.mark.parametrize("account_or_card_number, expected_result", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Mastercard 7000792289606361", "Mastercard 7000 79** **** 6361"),
    ("", "")
])
def test_mask_account_card(account_or_card_number, expected_result):
    assert mask_account_card(account_or_card_number) == expected_result


def test_wrong_data_mask_account_card():
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(123547467)

    assert str(exc_info.value) == "Некорректные данные"

@pytest.mark.parametrize('iso_date, expected_result', [
    ('2024-03-11T02:26:18.671407', '11.03.2024'),
    ('2025-04-11T02:26:18.671407', '11.04.2025'),
    ('', 'Неверный формат даты'),
    ('2025-04-1102:26:18.671407', 'Неверный формат даты')
])
def test_get_date(iso_date, expected_result):
    assert get_date(iso_date) == expected_result
