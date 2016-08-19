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

    # Applies a function to every node in the tree exactly once,
    # and returns a set of each resulting new tree.
    def apply(self, f):
        ret = set()
        applied = f(self)
        if not applied == None:
            ret.add(applied)
        for i in range(len(self.children)):
            newIthChildren = self.children[i].apply(f)
            for newChild in newIthChildren:
                newChildren = [child for child in self.children]
                newChildren[i] = newChild
                newNode = Node(self.data, *newChildren)
                ret.add(newNode)
        return ret

# Returns a node based upon a string expression.
# Right now, it assumes that the expression is well-formed.
def parse(exp):
    currData = ""
    openParendCount = 0
    children = []
    for i in range(len(exp)):
        if exp[i] == "(":
            if openParendCount == 0:
                startIndex = i
            openParendCount += 1
        elif exp[i] == ")":
            openParendCount -= 1
            if openParendCount == 0:
                children.append(parse(exp[startIndex + 1 : i]))
        elif openParendCount == 0:
            currData += exp[i]
    return Node(currData, *children)
