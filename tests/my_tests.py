from unittest import TestCase

from minigolf import HitsMatch, HolesMatch, Player
from standart_rules import StandRules


class StandClassTestCase(TestCase):
    def test_table(self):
        players = [Player('A'), Player('B'), Player('C')]
        m = HitsMatch(3, players)
        (self.assertEqual(m._table[0][0]._name, players[0]._name) for i in range(0, 2))

    def append_test(self):
        players = [Player('A'), Player('B'), Player('C')]
        m = HitsMatch(3, players)
        (self.assertEqual(m._table[0][i]._name, players[i]._name) for i in range(0, 2))
        listt = ['a', 'b', 'c']
        m.append_to_table(listt)
        self.assertEqual(m.get_table(), [
            ('A', 'B', 'C'),
            ('A', 'B', 'C'),
        ])
