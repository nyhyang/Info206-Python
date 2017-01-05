#---------------------------------------------------------
# Nancy Yang
# nancy_yang@berkeley.edu
# Homework #3
# September 20, 2016
# BST.py
# BST
# ---------------------------------------------------------

class Node:
    #Constructor Node() creates node
    def __init__(self,word):
        self.word = word
        self.right = None
        self.left = None
        self.count = 1

class BSTree:
    #Constructor BSTree() creates empty tree
    def __init__(self, root=None):
        # the root is the first word of the document
        self.root = root
    
    #These are "external functions" that will be called by your main program 
    # - I have given these to you
    
    #Find word in tree
    def find(self, word):
        # it goes to _find function and return the value of the function
        return _find(self.root, word)

    
    #Add node to tree with word
    def add(self, word):
        if not self.root:
            self.root = Node(word)
            return
        _add(self.root, word)

    #Print in order entire tree
    def in_order_print(self):
        _in_order_print(self.root)

    def size(self):
        return _size(self.root)

    def height(self):
        return _height(self.root)


#These are "internal functions" in the BSTree class - You need to create these!!!

#Function to add node with word as word attribute
def _add(root, word):
    if root.word == word:
        root.count +=1
        return
    if root.word > word:
        if root.left == None:
            root.left = Node(word)
        else:
            _add(root.left, word)
    else:
        if root.right == None:
            root.right = Node(word)
        else:
            _add(root.right, word)
    
#Function to find word in tree
def _find(root, word):
    if root == None:
        return 0
    if root.word == word:
        return root.count
    if root.word > word:
        return _find(root.left, word)
    else:
        return _find(root.right, word)


#Get number of nodes in tree
def _size(root):
    count = 0
    if root is not None:
        count = 1
    if root.left is not None:
        count += _size(root.left)
    if root.right is not None:
        count += _size(root.right)
    return count 

#Get height of tree
def _height(root):
    # A tree consisting only of one item (root) has a height of 1
    # An empty tree has a height of 0
    height = 0
    left_height = 0
    right_height = 0
    if root is not None:
        height = 1
    if root.left is not None:
        left_height += _height(root.left)
    if root.right is not None:
        right_height += _height(root.right)

    return height + max(left_height, right_height)

    
#Function to print tree in order
def _in_order_print(root): 
    # not sure what this is doing
    if not root: #if root == None #if root is None
        return
    _in_order_print(root.left)
    print(root.word)
    print(root.count)
    _in_order_print(root.right)
