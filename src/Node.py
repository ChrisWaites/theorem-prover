class Node(object):
    def __init__(self, data, *children):
        self.data = data
        self.children = children

    def __str__(self):
        if len(self.children) == 0:
            return self.data
        if len(self.children) == 1:
            return self.data + "(" + self.children[0].__str__() + ")"
        elif len(self.children) == 2:
            return "(" + self.children[0].__str__() + ")" + self.data + "(" + self.children[1].__str__() + ")"
        else:
            ret = self.data + "("
            for child in self.children:
                ret += child.__str__() + ","
            return ret[:-1] + ")"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.data == other.data and self.children == other.children
        return False

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self.data) ^ hash(self.children)

    def deepcopy(self):
        return Node(self.data, *(child.deepcopy() for child in self.children))

    def __cmp__(self, other):
        return cmp(len(self.__str__()), len(other.__str__()))

# Assumes well-formed expression
def parse(exp):
    if exp[0] == "~":
        return Node("~", parse(exp[2 : -1]))
    else:
        foundParend = False
        parendCount = 0
        operator = ""
        operatorIndex = -1
        for i in range(0, len(exp)):
            if exp[i] == "(":
                foundParend = True
                parendCount += 1
            elif exp[i] == ")":
                parendCount -= 1
            elif parendCount == 0:
                operator += exp[i]
                if operatorIndex == -1:
                    operatorIndex = i
        if not foundParend:
            return Node(exp)
        else:
            return Node(operator, parse(exp[1 : operatorIndex - 1]), parse(exp[operatorIndex + len(operator) + 1 : -1]))

def wellFormed(node):
    if node.data == "~":
        return len(node.children) == 1 and wellFormed(node.children[0])
    elif node.data in ["^", "v", "->", "<->"]:
        return len(node.children) == 2 and wellFormed(node.children[0]) and wellFormed(node.children[1])
    else:
        return len(node.children) == 0
