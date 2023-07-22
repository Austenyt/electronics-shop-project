from src.item import Item


class MixinLang:
    def __init__(self):
        self._language = "EN"

    @property
    def language(self):
        return self._language
    @language.setter
    def change_lang(self):
        if self.language == "EN":
            self._language = "RU"
        elif self.language == "RU":
            self._language = "EN"
        else:
            raise ValueError("Язык не опознан")


class Keyboard(Item, MixinLang):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

    def __str__(self):
        return f"{self.name}"

    @property
    def language(self):
        return self._language
