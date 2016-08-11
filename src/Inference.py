from Node import *

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
