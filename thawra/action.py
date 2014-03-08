import functools


class NotEnoughMana(Exception):
    pass


def attack(actor, target, cost, weather):
    for enemy in target:
        damage = (actor.stats['ATK'] - enemy.stats['DEF']) * 3
        enemy.hp -= damage


def magic(actor, target, cost, weather):
    if actor.mp < cost:
        raise NotEnoughMana
    else:
        actor.mp -= cost

    for enemy in target:
        damage = (actor.stats['MAG'] - enemy.stats['MDE']) * 3
        enemy.hp -= damage


class Action(object):

    effects = {
        'ATK': attack,
        'MAG': magic,
    }

    def __init__(self, actor, effect, target, cost):
        self.actor = actor

        # TODO(rahmu): Needs further validation
        self._effect = effect

        self.target = target
        self.cost = cost

    @property
    def effect(self):
        return functools.partial(self.effects[self._effect],
                                 self.actor,
                                 self.target,
                                 self.cost)

    def __call__(self, weather):
        self.effect(weather)
