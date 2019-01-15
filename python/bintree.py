
class Node:
    def __init__(self, value, weight=0):
        self.key = value

        self.weight = 0
        self.parent = None
        self.left = None
        self.right = None
        self.color = None


class BinaryTree:
    def __init__(self):
        self.origin = Node("0")
        self.nodes = {self.origin.key: self.origin}

    def addNode(self, parent, direction=0, weight=0):
        direction = str(direction)
        if direction:
            parent.left = Node(parent.key+direction)
            parent.left.parent = parent
            parent.left.weight = weight
            self.nodes[parent.left.key] = parent.left
        else:
            parent.right = Node(parent.key+direction)
            parent.right.parent = parent
            parent.right.weight = weight
            self.nodes[parent.right.key] = parent.right

    def height(self, node_key):
        select = self.nodes[node_key]
        h = 0
        while select.parent:
            h += 1
            select = select.parent
        return h

    def nodeValue(self, node_key):
        select = self.nodes[node_key]
        h = 0
        while select.parent:
            h += select.weight
            select = select.parent
        return h


class RBTree(BinaryTree):
    def __init__(self):
        self.origin = Node("0")
        self.origin.color = "black"
        self.nodes = {self.origin.key: self.origin}

    def addNode(self, parent, direction=0, weight=0):
        direction = str(direction)
        if parent.color == "black":
            color = "red"
        elif parent.color == "red":
            color = "black"
        if direction:
            parent.left = Node(parent.key+direction)
            parent.left.parent = parent
            parent.left.weight = weight
            parent.left.color = color
            self.nodes[parent.left.key] = parent.left
        else:
            parent.right = Node(parent.key+direction)
            parent.right.parent = parent
            parent.right.weight = weight
            parent.right.color = color
            self.nodes[parent.right.key] = parent.right
