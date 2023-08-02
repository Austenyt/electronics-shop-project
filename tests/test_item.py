"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv
import pytest
from src.item import Item


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price(), 200000
    assert item2.calculate_total_price(), 100000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    assert item1.price, 8000.0


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    item1 = Item.all[0]
    assert item1.price == 100
    assert item1.quantity == 1


def test_exp_from_csv_file():
    with pytest.raises(FileNotFoundError, match="Отсутствует файл items2.csv"):
        Item.instantiate_from_csv('../src/items.csv')
    with pytest.raises(ValueError, match="Файл item1.csv поврежден"):
        Item.instantiate_from_csv('../src/items.csv')


if __name__ == '__main__':
    pytest.main()
