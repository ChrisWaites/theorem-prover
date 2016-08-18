from Node import Node

# p
# (p)->(q)
# =>
# q
def modusPonens(nodeA, nodeB):
    if nodeB.data == "->" and nodeA == nodeB.children[0]:
        return nodeB.children[1]

# ~(q)
# (p)->(q)
# =>
# ~(p)
def modusTollens(nodeA, nodeB):
    if nodeA.data == "~" and nodeB.data == "->" and nodeA.children[0] == nodeB.children[1]:
        return Node("~", nodeB.children[0])

# (p)->(q)
# (q)->(r)
# =>
# (p)->(r)
def hypotheticalSyllogism(nodeA, nodeB):
    if nodeA.data == "->" and nodeB.data == "->" and nodeA.children[1] == nodeB.children[0]:
        return Node("->", nodeA.children[0], nodeB.children[1])

# (p)v(q)
# ~(p)
# =>
# q
def disjunctiveSyllogism(nodeA, nodeB):
    if nodeA.data == "v" and nodeB.data == "~" and nodeA.children[0] == nodeB.children[0]:
        return nodeA.children[1]

# p
# =>
# (p)v(q)
# def addition(node):
#     return Node("v", node, Node("q"))

# (p)^(q)
# =>
# p
def simplification(node):
    if node.data == "^":
        return node.children[0]

# p
# q
# =>
# (p)^(q)
def conjunction(nodeA, nodeB):
    return Node("^", nodeA, nodeB)

# (p)v(q)
# (~(p))v(r)
# =>
# (q)v(r)
def resolution(nodeA, nodeB):
    if nodeA.data == "v" and nodeB.data == "v":
        if nodeB.children[0].data == "~" and nodeA.children[0] == nodeB.children[0].children[0]:
            return Node("v", nodeA.children[1], nodeB.children[1])

# ((p)->(q))^((r)->(s))
# (p)v(r)
# =>
# (q)v(s)
def constructiveDilemma(nodeA, nodeB):
    if nodeA.data == "^":
        if nodeA.children[0].data == "->" and nodeA.children[1].data == "->":
            if nodeA.children[0].children[0] == nodeB.children[0] and nodeA.children[1].children[0] == nodeB.children[1]:
                return Node("v", nodeA.children[0].children[1], nodeA.children[1].children[1])

# (p)->(q)
# =>
# (p)->((p)^(q))
def absorption(node):
    if node.data == "->":
        return Node("->", node.children[0], Node("^", node.children[0], node.children[1]))
