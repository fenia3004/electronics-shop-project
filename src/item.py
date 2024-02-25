import csv
import os
from pathlib import Path


class InstantiateCSVError(Exception):
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    DATA_DIR = Path(__file__).parent.joinpath('items.csv')

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return str(self.__name)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        return None

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_cost = self.price * self.quantity

        return total_cost

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        """
        Геттер для приватного атрибута name.
        Возвращает значение приватного атрибута name.

        :return: Название товара.
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
        Сеттер для приватного атрибута name.
        Присваивает значение приватному атрибуту name.
        Если длина переданного значения больше 10 символов, обрезает его до 10 символов.

        :param value: Новое значение для названия товара.
        """
        name = value[:10]
        self.__name = name

    @classmethod
    def instantiate_from_csv(cls):
        """Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_"""
        try:
            with cls.DATA_DIR.open(newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                cls.all.clear()
                try:
                    for row in reader:
                        name = row['name']
                        price = row['price']
                        quantity = row['quantity']
                        cls(name, price, quantity)
                except KeyError:
                    raise InstantiateCSVError(f'Файл item.csv поврежден')
        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл item.csv')
        else:
            return cls


    @staticmethod
    def string_to_number(value: str) -> float:
        """Преобразует строку с числом в число."""
        return int(float(value))
