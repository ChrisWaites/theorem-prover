from expression import Expression

def quantifierInterchange(expr):
    """
    Ax(Ay(p(x, y))) <=> Ay(Ax(p(x, y)))
    Ex(Ey(p(x, y))) <=> Ey(Ex(p(x, y)))
    Ax(Ey(p(x, y))) <=> Ey(Ax(p(x, y)))
    Ex(Ay(p(x, y))) <=> Ay(Ex(p(x, y)))
    """
    if isinstance(expr.op, str):
        if expr.op[0] == "A" or expr.op[0] == "E":
            if expr.args[0].op[0] == "A" or expr.args[0].op[0] == "E":
                return Expression(expr.args[0].op , Expression(expr.op, expr.args[0].args[0]))

def quantifierNegation(expr):
    """
    Ex(~(p(x))) <=> ~(Ax(p(x)))
    Ax(~(p(x))) <=> ~(Ex(p(x)))
    """
    if expr.op == "~":
        if expr.args[0].op[0] == "A":
            return Expression("E" + expr.args[0].op[1:], ~expr.args[0].args[0])
        if expr.args[0].op[0] == "E":
            return Expression("A" + expr.args[0].op[1:], ~expr.args[0].args[0])
    if isinstance(expr.op, str):
        if expr.op[0] == "A" and expr.args[0].op == "~":
            return ~Expression("E" + expr.op[1:], expr.args[0].args[0])
        if expr.op[0] == "E" and expr.args[0].op == "~":
            return ~Expression("E" + expr.op[1:], expr.args[0].args[0])

def symmetryOfEquality(expr):
    """
    (x)=(y) <=> (y)=(x)
    """
    if expr.op == "=":
        return Expression("=", expr.args[1], expr.args[0])

def transitivityOfEquality(expr):
    """
    ((x)=(y))&((y)=(z)) <=> (x)=(z)
    """
    if expr.op == "&":
        if expr.args[0].op == "=" and expr.args[1].op == "=":
            if expr.args[0].args[1] == expr.args[1].args[0]:
                return Expression("=", expr.args[0].args[0], expr.args[1].args[1])

def addition(expr):
    """
    (x)=(y) <=> ((x)+(1))=((y)+(1))
    """
    if expr.op == "=":
        return Expression("=", expr.args[0] + Expression(1), expr.args[1] + Expression(1))

def subtraction(expr):
    """
     ((x)+(1))=((y)+(1)) <=> (x)=(y)
    """
    if expr.op == "=":
        if expr.args[0].op == "+" and expr.args[1].op == "+" and expr.args[0].args[1].op == 1 and expr.args[1].args[1].op == 1:
            return Expression("=", expr.args[0].args[0], expr.args[1].args[0])

def doubleNegationIntroduction(expr):
    """
    (x)=(y) <=> ~(~((x)=(y)))
    Ax(p(x)) <=> ~(~(Ax(p(x))))
    Ex(p(x)) <=> ~(~(Ex(p(x))))
    """
    if isinstance(expr.op, str):
        if expr.op == "=" or expr.op[0] == "A" or expr.op[0] == "E":
            return ~~expr
