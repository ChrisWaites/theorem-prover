import unittest
from theoremprover.search import *


class TestSearch(unittest.TestCase):

    def test_astar(self):
        neighbors = {
            'a': ['b', 'c'],
            'b': ['a', 'c'],
            'c': ['a', 'b', 'd'],
            'd': ['c']
        }
        g = Graph(neighbors)

        self.assertEquals(
            a_star(g, ['c'], lambda s: s == 'd'),
            ['c', 'd']
        )

        path = a_star(g, ['a'], lambda s: s == 'd')
        self.assertTrue(
            len(path) == 3 and path[0] == 'a' and path[2] == 'd'
        )

