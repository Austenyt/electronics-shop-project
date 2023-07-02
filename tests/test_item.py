"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

def test_calculate_total_price():
    assert item1.calculate_total_price(10000, 20) == 200000
    assert item2.calculate_total_price(20000, 5) == 100000


def test_apply_discount():
    assert item1.apply_discount(10000 * 0.8) == 8000.0
    assert item2.apply_discount(20000 * 0.8) == 16000.0