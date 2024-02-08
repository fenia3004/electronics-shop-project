from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, sim_card: int):
        """
        Создание экземпляра класса Phone и взятие экземпляров из род.класса
        """
        super().__init__(name, price, quantity)
        self._number_of_sim = None
        self.sim_card = sim_card

    def __repr__(self):
        return f'{super().__repr__()[:-1]}, {self.sim_card})'

    @property
    def number_of_sim(self):
        """
        Возвращает значение(кол-во) сим карт
        """
        return self.sim_card


    @number_of_sim.setter
    def number_of_sim(self, value) -> None:
        """
        Проверяет при переназначении кол-ва сим-карт на 0 и флоат. При положительном результете выдает ошибку
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self._number_of_sim = value