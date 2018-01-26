import unittest
from theoremprover.expression import Expression, parse


class TestExpression(unittest.TestCase):

    def test_parse(self):
        self.assertTrue(
            parse("T") == Expression("T")
        )

