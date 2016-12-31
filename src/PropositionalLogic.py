from Expr import Expr

def truth(expr):
    """
    T <=> ~(F)
    F <=> ~(T)
    """
    if expr.op == "T":
        return ~Expr("F")
    elif expr.op == "F":
        return ~Expr("T")
    elif expr.op == "~":
        if expr.args[0].op == "T":
            return Expr("F")
        elif expr.args[0].op == "F":
            return Expr("T")

def identity(expr):
    """
    (p)&(T) <=> p
    (p)|(F) <=> p
    """
    if expr.op == "&" and expr.args[1].op == "T":
        return expr.args[0]
    elif expr.op == "|" and expr.args[1].op == "F":
        return expr.args[0]

def domination(expr):
    """
    (p)|(T) <=> T
    (p)&(F) <=> F
    """
    if expr.op == "|" and expr.args[1].op == "T":
        return expr.args[1]
    elif expr.op == "&" and expr.args[1].op == "F":
        return expr.args[1]

def idempotent(expr):
    """
    (p)|(p) <=> p
    (p)&(p) <=> p
    """
    if expr.op == "&" or expr.op == "|":
        if expr.args[0] == expr.args[1]:
            return expr.args[0]

def doubleNegationIntroduction(expr):
    """
    p <=> ~(~(p))
    """
    if type(expr.op) == str and (expr.op in ("~", "&", "|", "->", "<->") or expr.op.isalpha()):
        return ~~expr

def doubleNegationElimination(expr):
    """
    ~(~(p)) <=> p
    """
    if expr.op == "~" and expr.args[0].op == "~":
        return expr.args[0].args[0]

def commutative(expr):
    """
    (p)|(q) <=> (q)|(p)
    (p)&(q) <=> (q)&(p)
    (p)<->(q) <=> (q)<->(p)
    """
    if expr.op == "|" or expr.op == "&" or expr.op == "<->":
        return Expr(expr.op, expr.args[1], expr.args[0])

def associative(expr):
    """
    ((p)&(q))&(r) <=> (p)&((q)&(r))
    ((p)|(q))|(r) <=> (p)|((q)|(r))
    ((p)<->(q))<->(r) <=> (p)<->((q)<->(r))
    """
    if (expr.op == "&" or expr.op == "|" or expr.op == "<->") and expr.op == expr.args[0].op:
        return Expr(expr.op, expr.args[0].args[0], Expr(expr.op, expr.args[0].args[1], expr.args[1]))

def distributive(expr):
    """
    (p)&((q)|(r)) <=> ((p)&(q))|((p)&(r))
    (p)|((q)|&(r)) <=> ((p)|(q))&((p)|(r))
    """
    if expr.op == "&" and expr.args[1].op == "|":
        if expr.args[0].op == "|" and expr.args[0].args[0] == expr.args[1].args[0]:
            return expr.args[0].args[0] | (expr.args[0].args[1] & expr.args[1].args[1])
        else:
            return (expr.args[0] & expr.args[1].args[0]) | (expr.args[0] & expr.args[1].args[1])
    elif expr.op == "|" and expr.args[1].op == "&":
        if expr.args[0].op == "&" and expr.args[0].args[0] == expr.args[1].args[0]:
            return expr.args[0].args[0] & (expr.args[0].args[1] | expr.args[1].args[1])
        else:
            return (expr.args[0] | expr.args[1].args[0]) & (expr.args[0] | expr.args[1].args[1])

def demorgans(expr):
    """
    ~((p)&(q)) <=> (~(p))|(~(q))
    ~((p)|(q)) <=> (~(p))&(~(q))
    """
    if expr.op == "~":
        if expr.args[0].op == "&":
            return ~expr.args[0].args[0] | ~expr.args[0].args[1]
        elif expr.args[0].op == "|":
            return ~expr.args[0].args[0] & ~expr.args[0].args[1]
    elif expr.op == "&":
        if expr.args[0].op == "~" and expr.args[1].op == "~":
            return ~(expr.args[0].args[0] | expr.args[1].args[0])
    elif expr.op == "|":
        if expr.args[0].op == "~" and expr.args[1].op == "~":
            return ~(expr.args[0].args[0] & expr.args[1].args[0])

def absorption(expr):
    """
    (p)&((p)|(q)) <=> p
    (p)|((p)&(q)) <=> p
    """
    if (expr.op == "&" and expr.args[1].op == "|") or (expr.op == "|" and expr.args[1].op == "&"):
        if expr.args[0] == expr.args[1].args[0]:
            return expr.args[0]

def negation(expr):
    """
    (p)|(~(p)) <=> T
    (p)&(~(p)) <=> F
    """
    if expr.op == "|":
        if expr.args[1].op == "~" and expr.args[0] == expr.args[1].args[0]:
            return Expr("T")
    elif expr.op == "&":
        if expr.args[1].op == "~" and expr.args[0] == expr.args[1].args[0]:
            return Expr("F")

def materialImplication(expr):
    """
    (p)->(q) <=> (~(p))|(q)
    (p)|(q) <=> (~(p))->(q)
    """
    if expr.op == "->":
        return ~expr.args[0] | expr.args[1]
    elif expr.op == "|":
        return ~expr.args[0] >> expr.args[1]

def contraposition(expr):
    """
    (p)->(q) <=> (~(q))->(~(p))
    """
    if expr.op == "->":
        return ~expr.args[1] >> ~expr.args[0]

def biconditional(expr):
    """
    (p)<->(q) <=> (~(p))<->(~(q))
    """
    if expr.op == "<->":
        return ~expr.args[0] % ~expr.args[1]

def biconditionalElimination(expr):
    """
    (p)<->(q) <=> ((p)->(q))&((q)->(p))
    """
    if expr.op == "<->":
        return (expr.args[0] >> expr.args[1]) & (expr.args[1] >> expr.args[0])
