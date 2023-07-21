from src.item import Item


class MixinLang:
    def __init__(self):
        self._language = "EN"

    @property
    def language(self):
        return self._language

    @language.setter
    def change_lang(self):
        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"
        return self


class Keyboard(Item, MixinLang):

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        super().__init__(language)

    def __str__(self):
        return f"{self._language}"
