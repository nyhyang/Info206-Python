from functools import reduce

numbers_rng = range(100,1000)
is_reversi = lambda numbers: str(numbers) == str(numbers)[::-1]
numbers_lst = [(x, y) for x in numbers_rng for y in numbers_rng ]

product_lst = [(x*y) for x in numbers_rng for y in numbers_rng]
reversi_num = list(filter(is_reversi, product_lst))
max_reversi = max(reversi_num)

numbers_tuple = list(filter( lambda item: item[0]* item[1] == max_reversi, numbers_lst))

print("{} x {} = {}".format(numbers_tuple[0][0], numbers_tuple[0][1], max_reversi))






#############################################################################
# def main():
	


# if __name__ == '__main__':
# 	main()