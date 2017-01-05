from functools import reduce

def is_reversi(numbers):
	if str(numbers) == str(numbers)[::-1]:
		return True
	else:
		return False

def find_reversi():
	number_lst = [0]
	xy_lst =[(0,0)]
	for x in range(999, 99, -1):
		for y in range(999, 99, -1):
			numbers = x * y
			if is_reversi(numbers) == True:
				if numbers > number_lst[0]:
					number_lst[0] = numbers
					xy_lst[0] = (x,y)
			else:
				continue
	
	print("{} x {} = {}".format(xy_lst[0][0], xy_lst[0][1], number_lst[0]))

#############################################################################

def main():
	find_reversi()


if __name__ == '__main__':
	main()