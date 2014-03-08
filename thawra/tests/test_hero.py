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

from thawra import hero


class HeroTest(unittest.TestCase):

    def setUp(self):
        self.hero = hero.Hero(name="",
                              skillmap="",
                              attributes=[8, 8, 3],
                              element="fire",
                              macros=None)

    def test_attributes(self):
        self.assertEqual(self.hero.strength, 8)
        self.assertEqual(self.hero.intelligence, 8)
        self.assertEqual(self.hero.agility, 3)

    def test_level(self):
        self.assertEqual(self.hero.level, 1)

    def test_hero_maxHP(self):
        return self.assertEqual(self.hero.hp, self.hero.intelligence * 100)

    def test_hero_maxMP(self):
        return self.assertEqual(self.hero.mp, self.hero.intelligence * 100)

    def test_hero_stats(self):
        return self.assertEqual(self.hero.stats, {
            'ATK': self.hero.strength * 10,
            'DEF': self.hero.strength * 2,
            'MAG': self.hero.intelligence * 7,
            'MDE': self.hero.intelligence * 2,
            'SPD': self.hero.agility * 30})

    def test_hero_hp(self):
        self.assertEqual(self.hero.hp, self.hero.maxHP)
        self.hero.hp -= self.hero.maxHP + 1
        self.assertEqual(self.hero.hp, 0)
        self.hero.hp += self.hero.maxHP * 2
        self.assertEqual(self.hero.hp, self.hero.maxHP)

    def test_invalid_attributes(self):
        self.assertRaises(hero.InvalidHero, hero.Hero,
                          "", "", [10], "", None)

if __name__ == "__main__":
    unittest.main()
