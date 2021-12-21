import abc
from abc import ABC
from random import choice


class AnimeMon(ABC):
    @property
    @abc.abstractmethod
    def exp(self):
        return self.experience

    @abc.abstractmethod
    def inc_exp(self, value):
        self.experience += value


class Digimon(AnimeMon):
    def __init__(self, name):
        self.name = name
        self.experience = 0

    def inc_exp(self, value):
        self.experience += value * 8

    @property
    def exp(self):
        return super().exp


class BasePokemon:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __str__(self):
        return f'{self.name}/{self.category}'


class EmojiMixin:
    emodji = {'grass': '🌿',
              'fire': '🔥',
              'water': '🌊',
              'electric': '⚡'}

    def __str__(self):
        text_category = super().__str__()
        return text_category.replace(self.category, self.emodji[self.category])


class Pokemon(AnimeMon, EmojiMixin, BasePokemon):
    def __init__(self, name, category):
        super().__init__(name, category)
        self.experience = 0

    def inc_exp(self, value):
        super().inc_exp(value)

    @property
    def exp(self):
        return super().exp


def train(animemon: AnimeMon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - animemon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = choice([True, False])
        if win:
            animemon.inc_exp(step_size)


if __name__ == '__main__':
    base = BasePokemon('abc', '123')
    print(base)

    digimon = Digimon('digi')
    print(digimon.exp)
    train(digimon)
    print(digimon.exp)

    pokemon = Pokemon('poke', 'fire')
    print(pokemon)

    pick = Pokemon('pick', 'water')
    print(pick)
