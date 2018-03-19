import unittest
from theoremprover.expression import Expression, parse


class TestExpression(unittest.TestCase):

    def test_parse(self):
        self.assertTrue(
            parse("T") == Expression("T")
        )
        
        self.assertTrue(
            parse("Aa(~(((a)+(1))=(0)))") == Expression('Aa', ~(Expression('=', Expression('a')+Expression(1), Expression(0))))
        )

