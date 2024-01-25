"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item = Item('name', 200.0, 2)
pay_rate = 0.85

def test_calculate_total_price():
    assert item.calculate_total_price() == 400
    assert type(item.calculate_total_price()) == float


def test_apply_discount():
    assert item.price * pay_rate == 170
