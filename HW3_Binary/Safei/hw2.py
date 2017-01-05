#---------------------------------------------------------
# <Safei (Fay) Gu>
# <sepahope@berkeley.edu>
# Homework #2
# September 15, 2015
# hw2.py
# Main
#---------------------------------------------------------

import re
from BST import *

#dont let others crash your file: invalid

def main():  # a main loop that takes as input a test word, and finds if it is in the BST

# load the work into the dictionary
	f = raw_input("Hello, user. "
    "\n Please type your file path with file name and press 'Enter':")
	wordss = open(f, 'r').read().split()
	#wordss = open('C:\Users\sepahope\Desktop\pg1342.txt').read().split()
#wordss = wordss.splitlines()
#First parameter is the replacement, second parameter is your input string
	i=0
	word2tree = []
	for i in range(0, len(wordss)):
		wordsss = re.compile('[^a-zA-Z]')
		x = wordsss.sub('', wordss[i])
		word2tree.append(x)
	word2tree = [y.lower() for y in word2tree]
	word2tree = filter(None, word2tree)
	#print len(word2tree) #124444


	T = BSTree()
	for i in range(0, len(word2tree)):
    #Functions for use
		T.add(word2tree[i])
    #T.find(word)
    #T.size()
    #T.height()
	
	#T.inOrderPrint() # this will print out the word of the text in the tree, 
	#and its count number(how many times)


	testword = ""
	while True:#(testword != "terminate"):
		testword = raw_input("Query?").lower()
		if testword == "stats":
		#print out the number of entries in the tree and the maximum depth of the tree.
			print "maximum depth of the tree: ", T.height()
			print "number of entries in the tree: ", T.size()
		elif testword == "terminate":
			print "Goodbye!"
			break
		else:
			T.find(testword)


if __name__ == "__main__": # when read this, stop running main?
	main()