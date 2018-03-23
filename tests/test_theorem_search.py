import unittest
from theoremprover.theorem_search import *
from theoremprover.expression import parse


class TestTheoremSearch(unittest.TestCase):

    def test_find_theorem(self):
        # simply passes by reaching a solution which terminates
        self.assertTrue(len(find_theorem(parse("~(Ea((0)=((a)+(1))))"))) >= 2)


