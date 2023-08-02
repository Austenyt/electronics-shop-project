import csv
import inspect
import os


class InstantiateCSVError(Exception):

    def __str__(self):
        return "Файл item.csv поврежден"


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)
        super().__init__()

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_length):
        if len(name_length) > 10:
            self.__name = name_length[:10]
        else:
            self.__name = name_length

    @classmethod
    def instantiate_from_csv(cls, filename='../src/items.csv'):
        cls.all.clear()
        try:
            with open(filename, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    try:
                        cls(row['name'], cls.string_to_number(row['price']), cls.string_to_number(row['quantity']))
                    except ValueError:
                        raise InstantiateCSVError()
        except FileNotFoundError:
            raise Exception("Отсутствует файл items.csv")

    @staticmethod
    def string_to_number(string):
        return int(float(string))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate
