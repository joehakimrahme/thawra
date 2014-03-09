
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import unittest

from thawra import battle
from thawra import hero


class BattleTest(unittest.TestCase):

    def setUp(self):
        self.hero11 = hero.Hero("11", "", (8, 8, 3), "fire", hero.randattack)
        self.hero12 = hero.Hero("12", "", (3, 8, 8), "fire", hero.randattack)
        self.hero13 = hero.Hero("13", "", (8, 3, 8), "fire", hero.randattack)
        self.hero21 = hero.Hero("21", "", (8, 5, 6), "fire", hero.randattack)
        self.hero22 = hero.Hero("22", "", (6, 8, 5), "fire", hero.randattack)
        self.hero23 = hero.Hero("23", "", (5, 6, 8), "fire", hero.randattack)

        self.team1 = [self.hero11, self.hero12, self.hero13]
        self.team2 = [self.hero21, self.hero22, self.hero23]

        self.battle = battle.Battle((self.team1, self.team2), "fire")

    def test_dead_or_alive(self):
        dead, alive = self.battle._dead_or_alive()

        self.assertEqual(len(dead), 0)
        self.assertEqual(len(alive), 2)

    def test_heroes(self):
        self.assertEqual(self.battle.heroes,
                         [self.hero11, self.hero12, self.hero13,
                          self.hero21, self.hero22, self.hero23])

    def test_enemies(self):
        self.assertEqual(self.battle.enemies(self.team1),
                         self.team2)

    def test_battle_loop(self):
        """Tests that the a pure randomattack battle ends.
        """
        self.battle.battle_loop()
        dead, alive = self.battle._dead_or_alive()
        self.assertEqual(len(dead), 1)
