class Node():
    def __init__(self):
        self.left = None
        self.right = None
        self.key = None
    
    def setLeft(self, left_node):
        self.left = left_node
    
    def setRight(self, right_node):
        self.right = right_node

    def setKey(self, key):
        self.key = key

    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right

    def getKey(self):
        return self.key

class BinarySearchTree():
    def __init__(self):
        self.root = None
    
    def setRoot(self, root):
        self.root = root
    
    def getRoot(self):
        return self.root

tree = BinarySearchTree()
node_1 = Node()
node_2 = Node()
node_3 = Node()
node_4 = Node()
node_5 = Node()
tree.setRoot(node_1)
node_1.setKey(22)
node_2.setKey(18)
node_3.setKey(15)
node_4.setKey(21)
node_5.setKey(16)
node_1.setLeft(node_2)
node_2.setLeft(node_3)
node_2.setRight(node_4)
node_3.setRight(node_5)

def find(tree, key):
    # Finds a node given the key value
    if tree.getRoot() == None:
        return None
    if tree.getRoot().getKey() == key:
        return tree.getRoot()
    elif key < tree.getRoot().getKey():
        tree.setRoot(tree.getRoot().getLeft())
        return find(tree, key)
    else:
        tree.setRoot(tree.getRoot().getRight())
        return find(tree, key)

def findMin(tree):
    # Assumption: tree is not empty
    if tree.getRoot().getLeft() == None:
        return tree.getRoot()
    else:
        tree.setRoot(tree.getRoot().getLeft())
        return findMin(tree)