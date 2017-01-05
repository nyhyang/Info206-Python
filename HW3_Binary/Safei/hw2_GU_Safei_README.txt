(0)  How you tested your program (what test cases and strategies did you use)
	During my coding process, the testing strategy I used is that I tested one tiny functional part of the program separately as I build up the whole program, in order to make sure every part could work before I combine them and test the whole code. 
	After that, I combined all the code together in BST.py and ran the following situations for .add function and .find function, with the strategy to test the BST.py first, tring to go through all the possible edge conditions (numeric/string in the tree, pass string/empty string/numeric value to the tree). 

T = BSTree()
T.add(6)
T.add(5)
T.add(8)
T.add(1)
T.add(5)
T.add(3)
print T.find("hellow")
print T.find(5)
print T.find(4)
print T.find(1)
print T.find("")
print T.find(" ")
print T.find("&")
print T.find("/")
print T.find("/* xx")
T.inOrderPrint()

T = BSTree()
T.add(4)
T.add(3)
T.add(2)
T.add(1)
T.add(1)
T.add(1)
print T.find("hellow")
print T.find(5)
print T.find(4)
print T.find(1)
print T.find(" ")
print T.find("&")
print T.find("/")
print T.find("/* xx")
T.inOrderPrint()

T = BSTree()
T.add("hellow")
T.add("goodby")
T.add("summer")
T.add("april")
T.add("lala")
T.add("hellow")
print T.find("hellow")
print T.find("lala")
print T.find(4)
print T.find("")
print T.find(" ")
print T.find("&")
print T.find("/")
print T.find("/* xx")
T.inOrderPrint()

	after testing the BST.py, I created a short txt file (see below in []) to test the hw2.py file to see if the text could be translated correctly into the desired format as a list, and also test to see if the number of the nodes and the height of the tree would work correctly for the short text file, before I move to officially test the long text file. Below is the short txt file I used to test, which includes multiple new lines, non-alphabetics within one word, and pure non-alphabetics which will be returned as an empty string in the list (got removed). For the queries, I used "stats", "in", "IN", "Errrrrror", "", " ", "xx /&", "*", "terminate" to try to make sure possible edge conditions would all work.

[It is a truth universall'y acknowledged, that a single man in possession
of a good fortune, 


must be in wa--nt of a wife.

However lit-111-tle ** **]


(1)  For the file http://www.gutenberg.org/cache/epub/1342/pg1342.txt what is the depth of your tree?  What does that say about the number of operations to find a word?
	28 is the depth of my tree. It means the maximum number of operations to find a word in this tree is 28.


(2)  What would happen if the input to your program were sorted (as it was in HW 1)?
	Then we will have a one-sided tree in the end, which only has all the data on either the right side or the left side of the tree, because every next value would be added to the same side of its parent node.


(3)  What are applications for binary search tree?  In what ways are they superior to lists?  In what ways are they inferior to lists?
	Binary search trees could store their elements in an insorted order, which is helpful for searching/sorting tasks. Binary search trees could also be applied to more complicated sorting/searching criterion or decision making situations.
	To use a binary search tree, it takes more effort to build the tree due to its more complicated structure, which is inferior to building lists, 
	while when using binary search tree to do search, since the tree is already sorted, it will take less effort to search for an item, which is superior than searching an unsorted list for that item.


(4)  Did you implement the extra credit?  
	No... Maybe will try it next time :p