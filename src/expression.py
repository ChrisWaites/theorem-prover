class Expression:
    """
    Represents an expression tree.

    op -- Is either a constant, a unary operator, or a binary operator
    args -- Is either 0, 1, or 2 Expressionession Trees, depending upon op
    """
    def __init__(self, op, *args, **kwargs):
        self.op = op
        self.args = args

    def __call__(self, *args):
        return Expression(self.op, *args)

    def __repr__(self):
        if len(self.args) == 0:
            return str(self.op)
        elif len(self.args) == 1:
            return str(self.op) + "(" + repr(self.args[0]) + ")"
        else:
            return "(" + repr(self.args[0]) + ")" + str(self.op) + "(" + repr(self.args[1]) + ")"

    def __eq__(self, other):
        if other is self:
            return True
        elif isinstance(other, Expression) and self.op == other.op:
            return self.args == other.args

    def __hash__(self):
        return hash(self.op) ^ hash(self.args)

    def __lt__(self, other):
        return Expression("<",  self, other)

    def __le__(self, other):
        return Expression("<=", self, other)

    def __ge__(self, other):
        return Expression(">=", self, other)

    def __gt__(self, other):
        return Expression(">",  self, other)

    def __add__(self, other):
        return Expression("+",  self, other)

    def __sub__(self, other):
        return Expression("-",  self, other)

    def __and__(self, other):
        return Expression("&",  self, other)

    def __div__(self, other):
        return Expression("/",  self, other)

    def __truediv__(self, other):
        return Expression("/",  self, other)

    def __invert__(self):
        return Expression("~",  self)

    def __lshift__(self, other):
        return Expression("<-", self, other)

    def __rshift__(self, other):
        return Expression("->", self, other)

    def __mul__(self, other):
        return Expression("*",  self, other)

    def __neg__(self):
        return Expression("-",  self)

    def __or__(self, other):
        return Expression("|",  self, other)

    def __pow__(self, other):
        return Expression("**", self, other)

    def __xor__(self, other):
        return Expression("^",  self, other)

    def __mod__(self, other):
        return Expression("<->",  self, other)

def parse(expr):
    """
    Takes in a string representation of an expression and returns and expression tree.
    Currently assumes a perfectly explicit expression, equivalent to repr(expr).
    Note that this entails perfectly explicit parenthesis.

    expr -- A string expression to be parsed. e.g. ~(~((p)|(q)))
    """
    op = ""
    args = []
    openParendCount = 0
    for i in range(len(expr)):
        if expr[i] == "(":
            if openParendCount == 0:
                startIndex = i
            openParendCount += 1
        elif expr[i] == ")":
            openParendCount -= 1
            if openParendCount == 0:
                args.append(parse(expr[startIndex + 1 : i]))
        elif openParendCount == 0:
            op += expr[i]
    if op.isdigit():
        op = int(op)
    return Expression(op, *args)
