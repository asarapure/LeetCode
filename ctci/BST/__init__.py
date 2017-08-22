class Node:

    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value == data:
            return False

        elif (self.value > data):
            if (self.left):
                return (self.left.insert(data))
            else :
                self.left = Node(data)

        elif (self.value < data):
            if (self.right):
                return (self.right.insert(data))
            else :
                self.right = Node(data)

    def preorder (self):
        if self:
            print(str(self.value))
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def inorder(self):
        if self :
            if self.left :
                self.left.inorder()
            print(str(self.value))
            if self.right :
                self.right.inorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(str(self.value))

class Tree:
    def __init__ (self, root):
        self.root = None

    def insert(self, data):
        if self.root :
            return(self.root.insert(data))
        else :
            self.root = Node(data)

    def preorder(self):
        if self.root is not None:
            self.root.preorder()

    def inorder(self):
        if self.root is not None :
            self.root.inorder()

    def postorder(self):
        if self.root is not None :
            self.root.postorder()


#has the long remove code here :- https://github.com/joeyajames/Python/blob/master/BinarySearchTree.py

