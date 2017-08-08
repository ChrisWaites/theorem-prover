from expression import Expression

def conjunction(exprA, exprB):
    """ Note that conjunction is necessarily a meta-operation.
    p
    q
    =>
    (p)&(q)
    """
    return exprA & exprB

def modusPonens(expr):
    """
    (p)&((p)->(q)) <=> q
    """
    if expr.op == "&":
        if expr.args[1].op == "->" and expr.args[0] == expr.args[1].args[0]:
            return expr.args[1].args[1]

def modusTollens(expr):
    """
    (~(q))&((p)->(q)) <=> ~(p)
    """
    if expr.op == "&":
        if expr.args[0].op == "~" and expr.args[1].op == "->" and expr.args[0].args[0] == expr.args[1].args[1]:
            return ~expr.args[1].args[0]

def hypotheticalSyllogism(expr):
    """
    ((p)->(q))&((q)->(r)) <=> (p)->(r)
    """
    if expr.op == "&":
        if expr.args[0].op == "->" and expr.args[1].op == "->" and expr.args[0].args[1] == expr.args[1].args[0]:
            return expr.args[0].args[0] >> expr.args[1].args[1]

def disjunctiveSyllogism(expr):
    """
    ((p)|(q))&(~(p)) <=> q
    """
    if expr.op == "&":
        if expr.args[0].op == "|" and expr.args[1].op == "~" and expr.args[0].args[0] == expr.args[1].args[0]:
            return expr.args[0].args[1]

# def addition(expr):
#     """
#     p <=> (p)|(q)
#     """
#     return expr | Expression("q")

def simplification(expr):
    """
    (p)&(q) <=> p
    """
    if expr.op == "&":
        return expr.args[0]

def resolution(expr):
    """
    ((p)|(q))&((~(p))|(r)) <=> (q)|(r)
    """
    if expr.op == "&":
        if expr.args[0].op == "|" and expr.args[1].op == "|":
            if expr.args[1].args[0].op == "~" and expr.args[0].args[0] == expr.args[1].args[0].args[0]:
                return expr.args[0].args[1] | expr.args[1].args[1]

def constructiveDilemma(expr):
    """
    (((p)->(q))&((r)->(s)))&((p)|(r)) <=> (q)|(s)
    """
    if expr.op == "&":
        if expr.args[0].op == "&":
            if expr.args[0].args[0].op == "->" and expr.args[0].args[1].op == "->":
                if expr.args[0].args[0].args[0] == expr.args[1].args[0] and expr.args[0].args[1].args[0] == expr.args[1].args[1]:
                    return expr.args[0].args[0].args[1] | expr.args[0].args[1].args[1]

def absorption(expr):
    """
    (p)->(q) <=> (p)->((p)&(q))
    """
    if expr.op == "->":
        return expr.args[0] >> (expr.args[0] & expr.args[1])
