from functools import reduce

# Text triangle to list of lists of ints, bottom to top
with open('triangle.txt', 'r') as f:
    text_tri = f.read()
    triangle = [list(map(int, x)) for x in [r.split(' ') for r in text_tri.split('\n')]][::-1]

t = reduce(lambda a, x: list(map(lambda x: (x[0],) + max(x[1], key=sum), # (x[0],) puts value from row being evaluated into one element tuple so it can be concatenated
                                 zip(x, zip(a, a[1:])))), # for x = [abc] and y = [defg] this returns [(ad), (ae), (be), (bf), ..., (cg)] http://stackoverflow.com/questions/20211024/how-to-iterator-over-every-2-overlapping-characters-in-a-string-of-dna-code
           triangle[1:], # Run through each row of the triangle, starting with the second-from-bottom row
           list(map(lambda x: (x,), triangle[0]))) # Initialize the reduce function with a list of tuples. Tuples are necessary in order to use (max(x, key=sum)), if x is an int it throws TypeError

# t is a one-element list containing a tuple of all of the values of the path, as ints
print(' + '.join(map(str, t[0])) + ' = ' + str(sum(t[0])))

