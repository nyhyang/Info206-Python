#---------------------------------------------------------
# Nancy Yang
# nancy_yang@berkeley.edu
# Homework #3
# September 20, 2016
# hw3test.py
# Test
#---------------------------------------------------------

from BST import *
from hw3 import *

T = BSTree()
T.add("4")
T.add("2")
T.add("3")
T.add("5")
T.add("1")
T.add("6")

T.in_order_print()

T.add("hello")
T.add("goodbye")
T.add("paul")
T.add("summer")
T.add("paul")
T.add("goodbye")

print(T.find("hello"))
print(T.size())
print(T.height())

T.in_order_print()