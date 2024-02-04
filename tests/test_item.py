"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item = Item('namenamename', 200.0, 2)
pay_rate = 0.85

short_name = "короткое"
long_name = "длинноеимяяяя"

item.name = short_name
assert item.name == short_name

item.name = long_name
assert item.name == long_name[:10]

def test_calculate_total_price():
    assert item.calculate_total_price() == 400
    assert type(item.calculate_total_price()) == float


def test_apply_discount():
    assert item.price * pay_rate == 170


def test_string_to_number():
    assert type(Item.string_to_number(item.price)) == int


def test__repr__():
    assert repr(item) == "Item('длинноеимя', 200.0, 2)"

def test__str__():
    assert str(item) == 'длинноеимя'