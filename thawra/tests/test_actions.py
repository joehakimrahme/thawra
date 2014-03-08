import unittest

from thawra.hero import Hero
from thawra.action import Action

class ActionTest(unittest.TestCase):

    def setUp(self):
        self.h1 = Hero("", "", (8, 8, 3), "fire", None)
        self.h2 = Hero("", "", (7, 2, 10), "fire", None)
        self.h3 = Hero("", "", (4, 5, 10), "fire", None)

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
