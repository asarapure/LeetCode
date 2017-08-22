class BinaryTree:
    def __init__(self, root):
        self.root = root

    def addLeft(self, data):
        current = self.root

        if current.left:
            current = self.root.left
            while current.left:
                current = current.left
            current.left = Node(data, None, None)
        self.root.left = Node(data, None, None)

    def addRight(self, data):
        if self.root.right:
            current = self.root.right
            while current.right:
                current = current.right
            current.right = Node(data, None, None)
        self.root.right = Node(data, None, None)

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right





n = Node(5, None, None)

btya = BinaryTree(n)
btya.addLeft(6)
btya.addRight(7)
btya.addLeft(3)






