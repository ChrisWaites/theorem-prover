from Node import Node

# Ax(Ay(p(x, y))) => Ay(Ax(p(x, y)))
# Ex(Ey(p(x, y))) => Ey(Ex(p(x, y)))
# Ax(Ey(p(x, y))) => Ey(Ax(p(x, y)))
# Ex(Ay(p(x, y))) => Ay(Ex(p(x, y)))
def quantifierInterchange(node):
    if node.data[0] == "A" or node.data[0] == "E":
        if node.children[0].data[0] == "A" or node.children[0].data[0] == "E":
            return Node(node.children[0].data , Node(node.data, node.children[0].children[0]))

# ~(Ax(p(x))) => Ex(~(p(x)))
# ~(Ex(p(x))) => Ax(~(p(x)))
# Ax(~(p(x))) => ~(Ex(p(x)))
# Ex(~(p(x))) => ~(Ax(p(x)))
def quantifierNegation(node):
    if node.data == "~":
        if node.children[0].data[0] == "A":
            return Node("E" + node.children.data[1:], Node("~", node.children[0].children[0]))
        if node.children[0].data[0] == "E":
            return Node("A" + node.children.data[1:], Node("~", node.children[0].children[0]))
    if node.data[0] == "A" and node.children[0].data == "~":
        return Node("~", Node("E" + node.data[1:], node.children[0].children[0]))
    if node.data[0] == "E" and node.children[0].data == "~":
        return Node("~", Node("E" + node.data[1:], node.children[0].children[0]))

# (x)=(y) => (y)=(x)
def symmetryOfEquality(node):
    if node.data == "=":
        return Node("=", node.children[1], node.children[0])

# (x)=(y) => (S(x))=(S(y))
def addition(node):
    if node.data == "=":
        return Node("=", Node("S", node.children[0]), Node("S", node.children[1]))

# (S(x))=(S(y)) => (x)=(y)
def subtraction(node):
    if node.data == "=":
        if node.children[0].data == "S" and node.children[1].data == "S":
            return Node("=", node.children[0].children[0], node.children[1].children[0])
