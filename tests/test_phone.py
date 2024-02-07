from src.phone import Phone

phone = Phone("iPhone 14", 120_000, 5, 2)

sim_card_1 = 0


def test__repr__():
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim():
    assert phone.number_of_sim == phone.sim_card


def test_number_of_sim_0():
    phone.sim_card = sim_card_1
    assert phone.sim_card == 0
