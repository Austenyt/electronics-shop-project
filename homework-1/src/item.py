class Item:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

  def calculate_total_price(self):
    return self.price * self.quantity

  def apply_discount(self):
    self.price = self.price * Item.pay_rate