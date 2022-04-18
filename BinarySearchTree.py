class Node():
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.key = None
    
    def setLeft(self, left):
        self.left = left
    
    def setRight(self, right):
        self.right = right

    def setParent(self, parent):
        self.parent = parent

    def setKey(self, key):
        self.key = key

    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right

    def getParent(self):
        return self.parent

    def getKey(self):
        return self.key

class BinarySearchTree():
    def __init__(self):
        self.root = None
    
    def setRoot(self, root):
        self.root = root
    
    def getRoot(self):
        return self.root
        
# set up for testing
tree = BinarySearchTree()
node_1 = Node()
node_2 = Node()
node_3 = Node()
node_4 = Node()
node_5 = Node()
node_6 = Node()
tree.setRoot(node_1)
node_1.setKey(22)
node_2.setKey(18)
node_3.setKey(15)
node_4.setKey(21)
node_5.setKey(16)
node_6.setKey(20)
node_1.setLeft(node_2)
node_2.setLeft(node_3)
node_2.setParent(node_1)
node_2.setRight(node_4)
node_3.setRight(node_5)
node_3.setParent(node_2)
node_4.setParent(node_2)
# end set up for testing

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

def treeInsert(tree, new_node):
    '''
    A BST only inserts elements to the leaves, so
    we insert by trarversing tree until we get to
    the place we need to insert the element
    '''
    record = None
    node_pivot = tree.getRoot()
    while node_pivot != None:
        record = node_pivot
        if new_node.getKey() < node_pivot.getKey():
            node_pivot = node_pivot.getLeft()
        else:
            node_pivot = node_pivot.getRight()
    new_node.setParent(record)
    if record == None:
        tree.setRoot(new_node)
    elif new_node.getKey() < record.getKey():
        record.setLeft(new_node)
    else:
        record.setRight(new_node)

def treeDelete(tree, node):
    '''
    If the node has no children, just delete
    If the node has 1 child, record the value 
    and set the node the that value, then delete
    the child
    If the node has 2 children, set the value of the node
    to the value of the right child, then move the pivot
    to the right child and tries to delete the right child.
    '''
    deleted = False
    pivot = tree.getRoot()
    while pivot.getKey() != node.getKey():
        if node.getKey() < pivot.getKey():
            pivot = pivot.getLeft()
        else:
            pivot = pivot.getRight()
    while deleted == False:
        if pivot.getLeft() == None and pivot.getRight() == None:
            if pivot.getKey() < pivot.getParent().getKey():
                pivot.getParent().setLeft(None)
            else:
                pivot.getParent().setRight(None)
            deleted = True
        elif pivot.getLeft() == None and pivot.getRight() != None:
            pivot.setKey(pivot.getRight().getKey())
            pivot.setRight(None)
            deleted = True
        elif pivot.getLeft() != None and pivot.getRight() == None:
            pivot.setKey(pivot.getLeft().getKey())
            pivot.setLeft(None)
            deleted = True
        else:
            pivot.setKey(pivot.getRight().getKey())
            pivot = pivot.getRight()

def treePrint_InOrder(tree):
    if tree.getRoot() != None:
        # not in pseudocode
        left_tree = BinarySearchTree()
        left_tree.setRoot(tree.getRoot().getLeft())
        right_tree = BinarySearchTree()
        right_tree.setRoot(tree.getRoot().getRight())
        # actual algorithm
        treePrint_InOrder(left_tree)
        print(tree.getRoot().getKey())
        treePrint_InOrder(right_tree)

def leftRotate(tree):
    '''
    We use rotation (in this case, left rotate)
    to balance a BST in an AVL tree. 
    That is to keep the runtime on the BST O(log n)
    We can use this to rotate any subtree also,
    not just the while tree
    '''
    root = tree.getRoot()
    new_root = root.getRight()
    root.setRight(new_root.getLeft())
    # root be parent of new_root's left node
    if new_root.getLeft() != None:
        new_root.getLeft().setParent(root)
    # set up new_root to be root of tree (or subtree)
    tree.setRoot(new_root)
    # parent of root is now parent of new_root
    new_root.setParent(root.getParent())
    # new_root is the child of root's old parent
    if root.getParent() != None:
        if root == root.getParent().getLeft():
            root.getParent().setLeft(new_root)
        else:
            root.getParent().setRight(new_root)
    # root is the left node of new_root
    # and new_root is the parent of root
    new_root.setLeft(root)
    root.setParent(new_root)