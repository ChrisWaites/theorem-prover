from Node import Node

def boolean(node):
    # T => ~(F)
    if node.data == "T":
        return Node("~", Node("F"))
    # F => ~(T)
    if node.data == "F":
        return Node("~", Node("T"))

def identity(node):
    # (p)^(T) => p
    if node.data == "^" and node.children[1].data == "T":
        return node.children[0]
    # (p)v(F) => p
    if node.data == "v" and node.children[1].data == "F":
        return node.children[0]

def domination(node):
    # (p)v(T) => T
    if node.data == "v" and node.children[1].data == "T":
        return Node("T")
    # (p)^(F) => F
    if node.data == "^" and node.children[1].data == "F":
        return Node("F")

def idempotent(node):
    # (p)v(p) => p
    # (p)^(p) => p
    if node.data == "^" or node.data == "v":
        if node.children[0] == node.children[1]:
            return node.children[0]

def introduceDoubleNegation(node):
    # p => ~(~(p))
    return Node("~", Node("~", node))

def removeDoubleNegation(node):
    # ~(~(p)) => p
    if node.data == "~" and node.children[0].data == "~":
        return node.children[0].children[0]

def commutative(node):
    # (p)v(q) => (q)v(p)
    # (p)^(q) => (q)^(p)
    # (p)<->(q) => (q)<->(p)
    if node.data == "v" or node.data == "^" or node.data == "<->":
        return Node(node.data, node.children[1], node.children[0])

def association(node):
    # ((p)^(q))^(r) => (p)^((q)^(r))
    if node.data == "^":
        if node.children[0].data == "^":
            return Node("^", node.children[0].children[0], Node("^", node.children[0].children[1], node.children[1]))
    # ((p)v(q))v(r) => (p)v((q)v(r))
    if node.data == "v":
        if node.children[0].data == "v":
            return Node("v", node.children[0].children[0], Node("^", node.children[0].children[1], node.children[1]))

def distribution(node):
    if node.data == "^":
        # (p)^((q)v(r)) => ((p)^(q))v((p)^(r))
        if node.children[1].data == "v":
            return Node("v", Node("^", node.children[0], node.children[1].children[0]), Node("^", node.children[0], node.children[1].children[1]))
    if node.data == "v":
        # (p)v((q)^(r)) => ((p)v(q))^((p)v(r))
        if node.children[1].data == "^":
            return Node("^", Node("v", node.children[0], node.children[1].children[0]), Node("v", node.children[0], node.children[1].children[1]))

def demorgans(node):
    if node.data == "~":
        # ~((p)^(q)) => (~(p))v(~(q))
        if node.children[0].data == "^":
            return Node("v", Node("~", node.children[0].children[0]), Node("~", node.children[0].children[1]))
        # ~((p)v(q)) => (~(p))^(~(q))
        if node.children[0].data == "v":
            return Node("^", Node("~", node.children[0].children[0]), Node("~", node.children[0].children[1]))
    if node.data == "^":
        # (~(p))^(~(q)) => ~((p)v(q))
        if node.children[0].data == "~" and node.children[1].data == "~":
            return Node("~", Node("v", node.children[0].children[0], node.children[1].children[0]))
    if node.data == "v":
        # (~(p))v(~(q)) => ~((p)^(q))
        if node.children[0].data == "~" and node.children[1].data == "~":
            return Node("~", Node("^", node.children[0].children[0], node.children[1].children[0]))

def absorption(node):
    if node.data == "^":
        if node.children[1].data == "v":
            # (p)^((p)v(q)) => p
            if node.children[0] == node.children[1].children[0]:
                return node.children[0]
    if node.data == "v":
        if node.children[1].data == "^":
            # (p)v((p)^(q)) => p
            if node.children[0] == node.children[1].children[0]:
                return node.children[0]

def negation(node):
    if node.data == "v":
        if node.children[1].data == "~":
            # (p)v(~(p)) => T
            if node.children[0] == node.children[1].children[0]:
                return Node("T")
    if node.data == "^":
        if node.children[1].data == "~":
            # (p)^(~(p)) => F
            if node.children[0] == node.children[1].children[0]:
                return Node("F")

def materialImplication(node):
    # (p)->(q) => (~(p))v(q)
    if node.data == "->":
        return Node("v", Node("~", node.children[0]), node.children[1])
    # (p)v(q) => (~(p))->(q)
    if node.data == "v":
        return Node("->", Node("~", node.children[0]), node.children[1])

def contraposition(node):
    # (p)->(q) => (~(q))->(~(p))
    if node.data == "->":
        return Node("->", Node("~", node.children[1]), Node("~", node.children[0]))

def biconditional(node):
    # (p)<->(q) => (~(p))<->(~(q))
    if node.data == "<->":
        return Node("<->", Node("~", node.children[0]), Node("~", node.children[1]))

def biconditionalElimination(node):
    # (p)<->(q) => ((p)->(q))^((q)->(p))
    if node.data == "<->":
        return Node("^", Node("->", node.children[0], node.children[1]), Node("->", node.children[1], node.children[0]))

def applyEquivalency(f, node):
    ret = []
    applied = f(node)
    if not applied == None:
        ret.append(applied)
    for i in range(len(node.children)):
        newIthChildren = applyEquivalency(f, node.children[i])
        for j in range(len(newIthChildren)):
            newChildren = [child for child in node.children]
            newChildren[i] = newIthChildren[j]
            newNode = Node(node.data, *newChildren)
            if not newNode == None:
                ret.append(newNode)
    return ret
