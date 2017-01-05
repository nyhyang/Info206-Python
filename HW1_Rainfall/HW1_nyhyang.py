# Body

def total_rain():
	"""find out the total usable data in the text file"""
	# read data from file and use data from each line
	with open('rainfall.txt', 'r') as fin:
		count_lst = []
		for lst_lines in fin:
			lst_lines = lst_lines.split(" ")
			# added " " after discussion with YiFei for the ' 2' case
			item = lst_lines[0]

			# check if the item is a number
			try:
				item = float(item)
			except ValueError:
				continue
			# make all the wanted number into a list
			if item >= 0:
				count_lst.append(item)
			elif int(item) == -999:
				break
		return count_lst
					

def average_rain(count_lst):
	"""use the organized list with only the number of rain falls wanted
	anything > 0 before the -999 
	and do the average"""
	total = sum(count_lst)
	total_num = len(count_lst)
	average = total / total_num
	# if the sum of the list is 0 it means that there is only 0 in the list
	if total == 0:
		print("Average rainfall = 0 inches")
	# if there is only -999 in the text file it will return empty list
	# therefore total_num will be 0
	elif total_num == 0:
		print("There are no valid rainfall inputs.")
	else:
		print("Average rainfall = {} inches".format(average))



def main():
	# total_rain()
	count_lst = total_rain()
	average_rain(count_lst)

if __name__ == '__main__':
	main()
