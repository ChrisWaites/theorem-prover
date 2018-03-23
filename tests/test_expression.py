import unittest
from theoremprover.expression import *


class TestExpression(unittest.TestCase):

    def test_init(self):
        # None case
        with self.assertRaises(ValueError):
            Expression(None)

        # Incorrect type case
        with self.assertRaises(ValueError):
            Expression(self)

        # Empty case
        with self.assertRaises(ValueError):
            Expression("")
        
        # Typical cases
        Expression('p')
        Expression(0)


    def test_parse(self):
        # None case
        with self.assertRaises(ValueError):
            parse(None)

        # Incorrect type case
        with self.assertRaises(ValueError):
            parse(self)

        # Empty case
        with self.assertRaises(ValueError):
            parse("")
        
        # Typical case
        self.assertEqual(
            parse("Aa(~(((a)+(1))=(0)))"),
            Expression('Aa', ~(Expression('=', Expression('a') + Expression(1), Expression(0))))
        )


    def test_ops(self):
        # unary
        self.assertEqual(
            ~Expression('p'),
            Expression('~', Expression('p'))
        )

        # binary
        self.assertEqual(
            Expression('p') ^ Expression('q'),
            Expression('^', Expression('p'), Expression('q'))
        )


