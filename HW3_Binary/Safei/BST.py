#---------------------------------------------------------
# <Safei (Fay) Gu>
# <sepahope@berkeley.edu>
# Homework #2
# September 15, 2015
# BST.py
# BST
#---------------------------------------------------------

class Node:
    #Constructor Node() creates node
    def __init__(self,word): 
    #Each node in the tree may keep track of the depth of the current subtree, 
    #and the number of entries below it?
        self.word = word
        self.right = None #REMOVE
        self.left = None
        self.count = 1 #depth?

class BSTree:
    #Constructor BSTree() creates empty tree
    def __init__(self, root=None):
        #WILL CREATE IN LAB
        self.root = root    
    #These are "external functions" that will be called by your main program - I have given these to you =)
    
    #Find word in tree
    def find(self, word):
        return _find(self.root, word)
    
    #Add node to tree with word
    def add(self, word):
        if not self.root:
            self.root = Node(word)
            return
        _add(self.root, word)

    #Print in order entire tree
    def inOrderPrint(self):
        _inOrderPrint(self.root)

    def size(self):
        return _size(self.root)

    def height(self):
        return _height(self.root)


#These are "internal functions" in the BSTree class - You need to create these!!!

#Function to add node with word as word attribute
# "_function name"is internal-use-only function, private ,not for outside programs to call
def _add(root, word): #only use this to build the txt into the tree,
    #YOU FILL THIS IN
    if root.word == word:#!!!!!!!!!!!!!!!checking if the string is empty, make sure it's not passed into the tree
        root.count += 1
        return
    elif root.word > word:
        if root.left == None: # if the node is pointing at left
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
    #YOU FILL THIS IN
    if root.word == word:
        print "The word ", word, "appears ", root.count, "times in the tree"
        #root.count += 1     # root.count already counted in .add
        return
    if root.word > word:
        if root.left == None:
            print "The word ", word, "doesn't appear in the tree"
            return
        else:
            _find(root.left, word)
    else:
        if root.right == None:
            print "The word ", word, "doesn't appear in the tree"
            return
        else:
            _find(root.right, word)



# What to do with empty string passed in


#Get number of nodes in tree: use the length of the list minus all the counts (4 a equals to 1 a)
def _size(root):
    #YOU FILL THIS IN
    if not root:
        return 0
    else:
        return 1+_size(root.right)+_size(root.left)

#Get height of tree

def _height(root):
    if root == None:
        return -1
    else:
        return 1+max(_height(root.right), _height(root.left))
    #YOU FILL THIS IN #max (right count, left count)
#-1
    
#Function to print tree in order
def _inOrderPrint(root):
    #YOU FILL THIS IN
    if not root:
        return # try to keep finding a note that's none, ASK AGAIN: second iphone photo
    _inOrderPrint(root.left)
    print root.word
    print root.count
    _inOrderPrint(root.right)

