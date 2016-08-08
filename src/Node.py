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
