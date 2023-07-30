"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv
import pytest
from src.item import Item
import pandas as pd


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


def test_exp_csv_file_corrupt():
    with pytest.raises(KeyError):

        with open('../src/items1.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Item(row['name'], Item.string_to_number(row['price']), Item.string_to_number(row['quantity']))


def test_instantiate_from_csv_corrupted_file():
    with pytest.raises(Exception, match="Файл items.csv поврежден"):
        Item.instantiate_from_csv()


def test_exp_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        pd.read_csv('../src/items2.csv')


if __name__ == '__main__':
    pytest.main()
