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
        elif self._language == "RU":
            self._language = "EN"
        else:
            raise ValueError("Язык не опознан")
        return self


class Keyboard(MixinLang, Item):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(_language)
        super().__init__(name, price, quantity)


    @property
    def language(self):
        return self._language

    def __str__(self):
        return f"{self._language}"
