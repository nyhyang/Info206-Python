import functools
from functools import reduce

# creates triangle
def create_triangle(data):
    listofrows = data.splitlines()
    listofrows = list(map(lambda x: x.split(), listofrows))
    triangle = [[int(x) for x in i] for i in listofrows]
    return(triangle)

# print(list(reversed(triangle[:-1])))
def updatemx(row, mx):  # updates row with max from row below
    mx = [row[i] + max(mx[i], mx[i+1]) for i in range(len(row))]
    mxList.append(mx)
    return mx

# creates list of directions
def dir(mx):
    direction = [l < r for l, r in zip(mx[:-1], mx[1:])]
    return direction

# creates path by appending points in triangle
def createPath(pos, path, directions, triangle):
    def pathAppend(pos, rowIndex):
        pos += directions[rowIndex][pos]
        path.append(triangle[1+rowIndex][pos])
        return pos
    reduce(lambda pos, x: pathAppend(pos, x), range(0, len(directions)), 0)

mxList = []
directions = []
pos = 0

def main():
    print("Enter the file name to read:")
    filename = input('> ')
    try:
        with open(filename, "r") as file:
            data = file.read()
    except IOError:
        print("Unable to open", filename, ".")
        print("Exiting.")
        sys.exit()
    triangle = create_triangle(data)
    mxList.append(triangle[-1])
    mx = reduce(lambda mx, row: updatemx(row, mx), reversed(triangle[:-1]), triangle[-1])
    maxdistance = str(mx[0])
    directions = list(map(lambda mx: dir(mx), mxList))
    directions.pop()
    directions.reverse()
    path = [triangle[0][0]]
    createPath(pos, path, directions, triangle)
    path = [str(x) for x in path]
    output = " + ".join(path)
    print("The maximum distance is", maxdistance)
    print("The optimal path is", output, " = ", maxdistance)

if __name__ == "__main__":
    main()
