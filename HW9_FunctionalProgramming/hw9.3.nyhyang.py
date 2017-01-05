def max_sum():
	num_lst = []
	total_lst = []
	try:
		with open('maxtriangle.txt', 'r') as fin:
			for line in fin:
				num_lst.append([int(x) for x in line.split()])
	
	except FileNotFoundError: 
		print('File not found.')
	
	for row in range(len(num_lst)-2, -1, -1):
		for column in range(0, row+1):
			num_lst[row][column] += max(num_lst[row+1][column], num_lst[row+1][column+1])
	
	max_num = num_lst[row][column]
	current_max = max_num 

	for row in range(len(num_lst)-1):
		for column in range(0, row+1):
			if num_lst[row][column] == current_max:
				total_lst.append(current_max - max(num_lst[row+1][column], num_lst[row+1][column+1]))
				current_max = max(num_lst[row+1][column], num_lst[row+1][column+1])
	total_lst.append(current_max)
	# print(total_lst)
	
	final_x = ""
	for x in total_lst:
		if x != total_lst[len(total_lst)-1]:
			final_x += str(x) + " + "
		else:
			final_x += str(x) + " = " + str(max_num)
		

	print(final_x)





	
# 		for numbers in range(1, len(line)):
# 			numbers = int(numbers)
# 			#start from the second line to add to the first line
# 			# all the left side -- remain one route all the way down
# 			line[numbers][0]+= line[numbers-1][0]
# 			# find the max sum of the middle 
# 			width = len(lines[numbers]) 
# 			for mid_num in range(1, width-1):
# 				line[numbers][mid_num]+= max(line[numbers-1][mid_num], line[numbers-1][mid_num-1])
# 			# right side -- remain one route all the way down
# 			line[numbers][width-1]+= line[numbers-1][width-2]




#############################################################################
def main():

	max_sum()






if __name__ == '__main__':
	main()


