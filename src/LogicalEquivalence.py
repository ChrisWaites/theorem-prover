from Node import Node

# T <=> ~(F)
# F <=> ~(T)
def truth(node):
    if node.data == "T":
        return Node("~", Node("F"))
    if node.data == "F":
        return Node("~", Node("T"))
    if node.data == "~":
        if node.children[0].data == "T":
            return Node("F")
        if node.children[0].data == "F":
            return Node("T")

# (p)^(T) <=> p
# (p)v(F) <=> p
def identity(node):
    if node.data == "^" and node.children[1].data == "T":
        return node.children[0]
    if node.data == "v" and node.children[1].data == "F":
        return node.children[0]

# (p)v(T) <=> T
# (p)^(F) <=> F
def domination(node):
    if node.data == "v" and node.children[1].data == "T":
        return Node("T")
    if node.data == "^" and node.children[1].data == "F":
        return Node("F")

# (p)v(p) <=> p
# (p)^(p) <=> p
def idempotent(node):
    if node.data == "^" or node.data == "v":
        if node.children[0] == node.children[1]:
            return node.children[0]

# p <=> ~(~(p))
def doubleNegationIntroduction(node):
    if node.data in ["~", "^", "v", "->", "<->"]:
        return Node("~", Node("~", node))

# p <=> ~(~(p))
def doubleNegationElimination(node):
    if node.data == "~" and node.children[0].data == "~":
        return node.children[0].children[0]

# (p)v(q) <=> (q)v(p)
# (p)^(q) <=> (q)^(p)
# (p)<->(q) <=> (q)<->(p)
def commutative(node):
    if node.data == "v" or node.data == "^" or node.data == "<->":
        return Node(node.data, node.children[1], node.children[0])

# ((p)^(q))^(r) <=> (p)^((q)^(r))
# ((p)v(q))v(r) <=> (p)v((q)v(r))
def association(node):
    if node.data == "^":
        if node.children[0].data == "^":
            return Node("^", node.children[0].children[0], Node("^", node.children[0].children[1], node.children[1]))
    if node.data == "v":
        if node.children[0].data == "v":
            return Node("v", node.children[0].children[0], Node("^", node.children[0].children[1], node.children[1]))

# (p)^((q)v(r)) <=> ((p)^(q))v((p)^(r))
# (p)v((q)^(r)) <=> ((p)v(q))^((p)v(r))
def distribution(node):
    if node.data == "^":
        if node.children[1].data == "v":
            if node.children[0].data == "v" and node.children[0].children[0] == node.children[1].children[0]:
                return Node("v", node.children[0].children[0], Node("^", node.children[0].children[1], node.children[1].children[1]))
            return Node("v", Node("^", node.children[0], node.children[1].children[0]), Node("^", node.children[0], node.children[1].children[1]))
    if node.data == "v":
        if node.children[1].data == "^":
            if node.children[0].data == "^" and node.children[0].children[0] == node.children[1].children[0]:
                return Node("^", node.children[0].children[0], Node("v", node.children[0].children[1], node.children[1].children[1]))
            return Node("^", Node("v", node.children[0], node.children[1].children[0]), Node("v", node.children[0], node.children[1].children[1]))

# ~((p)^(q)) <=> (~(p))v(~(q))
# ~((p)v(q)) <=> (~(p))^(~(q))
def demorgans(node):
    if node.data == "~":
        if node.children[0].data == "^":
            return Node("v", Node("~", node.children[0].children[0]), Node("~", node.children[0].children[1]))
        if node.children[0].data == "v":
            return Node("^", Node("~", node.children[0].children[0]), Node("~", node.children[0].children[1]))
    if node.data == "^":
        if node.children[0].data == "~" and node.children[1].data == "~":
            return Node("~", Node("v", node.children[0].children[0], node.children[1].children[0]))
    if node.data == "v":
        if node.children[0].data == "~" and node.children[1].data == "~":
            return Node("~", Node("^", node.children[0].children[0], node.children[1].children[0]))

# (p)^((p)v(q)) <=> p
# (p)v((p)^(q)) <=> p
def absorption(node):
    if node.data == "^":
        if node.children[1].data == "v":
            if node.children[0] == node.children[1].children[0]:
                return node.children[0]
    if node.data == "v":
        if node.children[1].data == "^":
            if node.children[0] == node.children[1].children[0]:
                return node.children[0]

# (p)v(~(p)) <=> T
# (p)^(~(p)) <=> F
def negation(node):
    if node.data == "v":
        if node.children[1].data == "~":
            if node.children[0] == node.children[1].children[0]:
                return Node("T")
    if node.data == "^":
        if node.children[1].data == "~":
            if node.children[0] == node.children[1].children[0]:
                return Node("F")

# (p)->(q) <=> (~(p))v(q)
# (p)v(q) <=> (~(p))->(q)
def materialImplication(node):
    if node.data == "->":
        return Node("v", Node("~", node.children[0]), node.children[1])
    if node.data == "v":
        return Node("->", Node("~", node.children[0]), node.children[1])

# (p)->(q) <=> (~(q))->(~(p))
def contraposition(node):
    if node.data == "->":
        return Node("->", Node("~", node.children[1]), Node("~", node.children[0]))

# (p)<->(q) <=> (~(p))<->(~(q))
def biconditional(node):
    if node.data == "<->":
        return Node("<->", Node("~", node.children[0]), Node("~", node.children[1]))

# (p)<->(q) <=> ((p)->(q))^((q)->(p))
def biconditionalElimination(node):
    if node.data == "<->":
        return Node("^", Node("->", node.children[0], node.children[1]), Node("->", node.children[1], node.children[0]))
