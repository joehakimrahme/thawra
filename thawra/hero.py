from thawra import action

class InvalidHero(Exception):
    def __init__(self, msg, value):
        self.value = value
        self.msg = msg

    def __str__(self):
        return self.msg


class Hero(object):

    def __repr__(self):
        return self.name

    def __init__(self, name, skillmap, attributes, element, macros=None):
        self.name = name
        self.element = element

        if len(attributes) != 3 or \
           not all(map(lambda x: isinstance(x, int), attributes)):
            raise InvalidHero(
                "Expected array of 3 integers for attributes, got: %s" % attributes,
                attributes)
        self.attributes = dict(zip(('str', 'int', 'agi'), attributes))

        # TODO: validate skillmap input
        self.skillmap = skillmap

        # TODO: validate macros input
        self.macros = macros

        self.status = None

        self.stats = {
            'ATK': self.strength * 10,
            'DEF': self.strength * 2,
            'MAG': self.intelligence * 7,
            'MDE': self.intelligence * 2,
            'SPD': self.agility * 30
        }

        self.maxHP = self.strength * 100
        self.maxMP = self.intelligence * 100
        self._hp = self.maxHP
        self._mp = self.maxMP

        # TODO: fill the rest of the dict with the skills
        self.actions = {
            'ATK': lambda target: action.Action(self, 'ATK', target, 0),
            'MAG': lambda target: action.Action(self, 'MAG', target, self.maxMP / 15)
        }

    @property
    def level(self):
        return self._get_level()

    @property
    def strength(self):
        return self.attributes['str']

    @property
    def intelligence(self):
        return self.attributes['int']

    @property
    def agility(self):
        return self.attributes['agi']

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        switch = {
            True: value,
            value > self.maxHP: self.maxHP,
            value < 0: 0}

        self._hp = switch[True]

    @property
    def mp(self):
        return self._mp

    @mp.setter
    def mp(self, value):
        switch = {
            True: value,
            value > self.maxHP: self.maxHP,
            value < 0: 0}


        self._mp = switch[True]

    def _get_level(self):
        #TODO: it should be a max between this and the highest skill
        #TODO: it should raise an InvalidHero exception in case of a problem
        return sum(self.attributes.values()) / 10
