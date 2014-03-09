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

import random
import unittest

from thawra import hero


class ActionTest(unittest.TestCase):

    def setUp(self):
        self.h1 = hero.Hero("H1", "", (8, 8, 3), "fire", None)
        self.h2 = hero.Hero("H2", "", (7, 2, 10), "fire", None)
        self.h3 = hero.Hero("H3", "", (4, 5, 10), "fire", None)

    def test_attack(self):
        self.h1.actions['ATK']([self.h2])("")
        self.assertNotEqual(self.h2.hp, self.h2.maxHP)
        self.assertEqual(self.h1.mp, self.h1.maxMP)

    def test_magic(self):
        self.h1.actions['MAG']([self.h2])("")
        self.assertNotEqual(self.h2.hp, self.h2.maxHP)
        self.assertNotEqual(self.h1.mp, self.h1.maxMP)

    def test_attack_twice(self):
        self.h1.actions['ATK']([self.h2, self.h2])("")
        self.assertNotEqual(self.h2.hp, self.h2.maxHP)
        self.assertEqual(self.h1.mp, self.h1.maxMP)

    def test_attack_multiple(self):
        self.h1.actions['ATK']([self.h2, self.h3])("")
        self.assertNotEqual(self.h2.hp, self.h2.maxHP)
        self.assertNotEqual(self.h3.hp, self.h3.maxHP)
        self.assertEqual(self.h1.mp, self.h1.maxMP)

    def test_magic_twice(self):
        self.h1.actions['MAG']([self.h2, self.h2])("")
        self.assertNotEqual(self.h2.hp, self.h2.maxHP)
        self.assertNotEqual(self.h1.mp, self.h1.maxMP)

    def test_magic_multiple(self):
        self.h1.actions['MAG']([self.h2, self.h3])("")
        self.assertNotEqual(self.h2.hp, self.h2.maxHP)
        self.assertNotEqual(self.h3.hp, self.h3.maxHP)
        self.assertNotEqual(self.h1.mp, self.h1.maxMP)


if __name__ == "__main__":
    unittest.main()
