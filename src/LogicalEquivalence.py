def apply(node, f):
    ret = []
    applied = f(node)
    if not applied == node:
        ret.append(applied)
    for i in range(len(node.children)):
        newIthChildren = node.children[i].apply(f)
        for j in range(len(newIthChildren)):
            newChildren = [child for child in node.children]
            newChildren[i] = newIthChildren[j]
            newNode = Node(node.data, *newChildren)
            if not newNode == node:
                ret.append(newNode)
    return ret

def identity(node):
    if node.data == "^" and node.children[1] == "T":
        return node.children[0]
    if node.data == "v" and node.children[1] == "F":
        return node.children[0]
    return node

def domination(node):
    if node.data == "v" and node.children[1] == "T":
        return node.children[0]
    if node.data == "^" and node.children[1] == "F":
        return node.children[0]
    return node

def idempotent(node):
    if node.data == "^" or node.data == "v":
        if node.children[0] == node.children[1]:
            return node.children[0]
    return node

def introduceDoubleNegation(node):
    return Node("~", Node("~", node))

def removeDoubleNegation(node):
    if node.data == "~" and node.children[0].data == "~":
        return node.children[0].children[0]
    return node

def commutative(node):
    if node.data == "v" or node.data == "^" or node.data == "<->":
        return Node(node.data, node.children[1], node.children[0])
    return node

# def associative(node):
#     # TODO: implement
#
# def distributive(node):
#     # TODO: implement

def demorgans(node):
    if node.data == "~":
        if node.children[0].data == "^":
            return Node("v", Node("~", node.children[0]), Node("~", node.children[1]))
        if node.children[0].data == "v":
            return Node("^", Node("~", node.children[0]), Node("~", node.children[1]))
    if node.data == "^" or node.data == "v":
        if node.children[0].data == "~" and node.children[1].data == "~":
            if node.data == "^":
                return Node("~", Node("v", node.children[0].children[0], node.children[1].children[0]))
            if node.data == "v":
                return Node("~", Node("^", node.children[0].children[0], node.children[1].children[0]))
    return node

# def absorption(node):
#     # TODO: implement

def negation(node):
    if node.data == "v":
        if node.children[1].data == "~":
            if node.children[0] == node.children[1].children[0]:
                return Node("T")
    if node.data == "^":
        if node.children[1].data == "~":
            if node.children[0] == node.children[1].children[0]:
                return Node("F")
    return node

def materialImplication(node):
    if node.data == "->":
        return Node("v", Node("~", node.children[0]), node.children[1])
    if node.data == "v":
        return Node("->", Node("~", node.children[0]), node.children[1])
    return node

def contrapositive(node):
    if node.data == "->":
        return Node("->", Node("~", node.children[1]), Node("~", node.children[0]))
    return node

def biconditional(node):
    if node.data == "<->":
        return Node("<->", Node("~", node.children[0]), Node("~", node.children[1]))
    return node

def biconditionalElimination(node):
    if node.data == "<->":
        return Node("^", Node("->", node.children[0], node.children[1]), Node("->", "->", node.children[1], node.children[0]))
    return node
