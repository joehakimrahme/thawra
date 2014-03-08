import unittest

from thawra import battle
from thawra import hero


class BattleTest(unittest.TestCase):

    def setUp(self):
        self.hero11 = hero.Hero("11", "", (8, 8, 3), "fire", None)
        self.hero12 = hero.Hero("12", "", (3, 8, 8), "fire", None)
        self.hero13 = hero.Hero("13", "", (8, 3, 8), "fire", None)
        self.hero21 = hero.Hero("21", "", (8, 5, 6), "fire", None)
        self.hero22 = hero.Hero("22", "", (6, 8, 5), "fire", None)
        self.hero23 = hero.Hero("23", "", (5, 6, 8), "fire", None)

        self.team1 = (self.hero11, self.hero12, self.hero13)
        self.team2 = (self.hero21, self.hero22, self.hero23)

        self.battle = battle.Battle((self.team1, self.team2), "fire")

    def test_dead_or_alive(self):
        dead, alive = self.battle._dead_or_alive()

        self.assertEqual(len(dead), 0)
        self.assertEqual(len(alive), 2)
