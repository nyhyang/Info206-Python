#---------------------------------------------------------
# Nancy Yang
# nancy_yang@berkeley.edu
# Homework #3
# September 20, 2016
# hw3.py
# Main
#---------------------------------------------------------

from BST import *

def read_file(filename):
    with open(filename, 'rU') as document:
        text = document.read()
    filter_punc = lambda t: ''.join([x.lower() for x in t if x.isalpha()])
    words = [x for x in map(filter_punc, text.split()) if x]
    return words


def main():
    while(True):
        print("Enter the file name to read:")
        filename = input('> ')
        try:
            words = read_file(filename)
        except IOError:
            print("Unable to find the file {}".format(filename))
        else:
            tree = BSTree()
            for word in words:
                tree.add(word)
            break

    ######################
    # Begin Student Code #
    ######################
    #Functions for use
    # tree.add(word):

    while(True):
        word = str(input("Query?"))
        if  word == 'terminate':
            break
        elif word == 'stats':
            node_size = tree.size()
            max_height =tree.height()
            print('The number of the entries of the tree is {}.'.format(node_size))
            print('The maximun height of the tree is {}.'.format(max_height))
        
        else:
            number_count = tree.find(word)
            print("The word {} appears {} times in the tree.".format(word, number_count))
 

    # tree.inOrderPrint():


if __name__ == "__main__":
    main()