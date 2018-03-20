import unittest
from theoremprover.expression import Expression, parse


class TestExpression(unittest.TestCase):

    def test_parse(self):
        self.assertEqual(
            parse("T"),
            Expression("T")
        )
        
        self.assertEqual(
            parse("Aa(~(((a)+(1))=(0)))"),
            Expression('Aa', ~(Expression('=', Expression('a')+Expression(1), Expression(0))))
        )

    def test_ops(self):
        self.assertEqual(
            Expression('^', Expression('a'), Expression('b')),
            Expression('a') ^ Expression('b')
        )

