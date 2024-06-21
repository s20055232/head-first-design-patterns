from abc import ABC, abstractmethod
from itertools import product


class WeaponBehavior(ABC):
    @abstractmethod
    def use_weapon(self):
        raise NotImplementedError


class SwordBehavior(WeaponBehavior):
    def use_weapon(self):
        return 5


class KnifeBehavior(WeaponBehavior):
    def use_weapon(self):
        return 3


class BowAndArrowBehavior(WeaponBehavior):
    def use_weapon(self):
        return 4


class AxeBehavior(WeaponBehavior):
    def use_weapon(self):
        return 2


class Character(ABC):
    def __init__(self) -> None:
        self._weapon = SwordBehavior()

    @property
    def weapon(self):
        return self._weapon

    @weapon.setter
    def weapon(self, value: WeaponBehavior):
        self._weapon = value

    def fight(self):
        return self._weapon.use_weapon()


class King(Character):
    pass


class Queen(Character):
    pass


class Knight(Character):
    pass


class Troll(Character):
    pass


def battle(p1: Character, p2: Character):
    return (
        f"{p1.__class__.__name__} win"
        if p1.fight() > p2.fight()
        else f"{p2.__class__.__name__} win"
    )


k = King()
k.weapon = SwordBehavior()
q = Queen()
q.weapon = KnifeBehavior()
kn = Knight()
kn.weapon = BowAndArrowBehavior()
t = Troll()
t.weapon = AxeBehavior()

for i in product([k, q, kn, t], repeat=2):
    print(battle(*i))
