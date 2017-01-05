# Import
import urllib.request as re;
import urllib.error as er;
import string
import operator

# Body
def match_dict():
	"""create a dictionary from the txt file and add index to it"""
	books_dict = {}
	book_titlelst = []
	http = 'http://'
	https = 'https://'
	book_title = ""
	idx = 0
	try:
		with open('hw4simplecatalog.txt', 'r') as fin:
			lines = fin.readlines()
	except FileNotFoundError: 
		print('File not found.')
	else:	
		for line in lines:
			line = line.strip()
			value_lst = []
			"""use keyword to separate url from book title, 
			can't use splitlines(',') cus there might be , in the titles 
			eg me,myself and I"""
			# find http and if there is no, it will continue to the next line
			try:
				if http in line or https in line:
					#http_index = line.index(http)
					
					# -1 to get things before comma
					#book_title = line[:http_index - 1]
					try:
						# if (http_index == 0 or line[http_index-1] != ',') and line[:http_index-2] == '' :
						# 	continue
						book_lst = line.rsplit(',', 1)
						# print(len(book_lst))
						if len(book_lst) == 2 and (http in book_lst[1] or https in book_lst[1]) and book_lst[0] != '' and book_lst[1] != '' :
							book_title = book_lst[0]
							url = book_lst[1]
							value_lst.append(idx)
							value_lst.append(url)
						if book_title not in books_dict:
							book_titlelst.append(book_title)
							idx += 1
						if book_title not in books_dict:
							books_dict[book_title] = value_lst
							book_titlelst.append(book_title)


					except:
						continue
						

				# elif https in line:
				# 	https_index = line.index(https)
				# 	url = line[https_index:].strip()
				# 	value_lst.append(idx)
				# 	value_lst.append(url)
				# 	book_title = line[:https_index - 1]

				# 	if book_title not in books_dict:
				# 		book_titlelst.append(book_title)
				# 		idx += 1
			except: 
				continue

		# print(books_dict)
		read_books(books_dict, book_titlelst)
		
							

def read_books(books_dict, book_titlelst):
	"""open books from the url"""
	index_lst = []
	url_lst = []
	words_dict = {}
	total_books = len(books_dict)
	for key, value in books_dict.items():
		# unpack the tuple into a list
		try:
			book_index = value[0]
			url = value[1]
		except:
			continue
	 		
		try:
			#open url, response = the webpage
			response = re.urlopen(url)
			#get data, content = the texts in the page
			content = response.read().decode('utf-8')
			#close connection 
			response.close()
		except(er.URLError):
			content = ""
			print("The url is not functional: " + url)
		# list of cleaned data from filter_data function
		list_of_words = filter_data(content)
		
		words_dict = word_count(list_of_words, words_dict, book_index, total_books)
	# print(words_dict)
	search_dict(books_dict, words_dict, book_titlelst)

def filter_data(text):
	""""filter out non alphabets
	 converting upper-case letters to lower-case letters and discarding punctuation
     and count the words."""
	#remove empty spaces
	list_of_words = text.split()
	#remove non-alphabetical characters
	list_of_words = [''.join([char for char in word if char in string.ascii_letters]).lower() for word in list_of_words]
	# check if the word is only alphabets
	list_of_words = [word for word in list_of_words if word.isalpha()]
	return list_of_words
 

def word_count(list_of_words, words_dict, book_index, total_books):
	"""to create a dict of word count in each url"""
	# words_dict {word : [1, 0 , 0]}

	for eachword in list_of_words:
		# add the word into the dictionary if it's not in it
		if eachword not in words_dict:
			# to create a list of counts with fix length with total books
			WordCounts = [0] * total_books
			# increments the values for corresponding index by one to indicate the word exists
			WordCounts[book_index] += 1
			# to make the word the key and lists of count as value for the dict
			words_dict[eachword] =  WordCounts 
		else: 
			""" if the word alread exists"""
			# find the count lists that exists
			WordCounts = words_dict[eachword] 
			# update the count that aligns to the book index
			WordCounts[book_index] += 1
			# assign the updated value list back to the dict
			words_dict[eachword] =  WordCounts 
	return words_dict


def search_dict(books_dict, words_dict, book_titlelst):
	
	while True:
		user_word = input("Search term? ")
		if user_word == "<terminate>":
			break
		elif user_word == '<catalog>':
			for book_title,value in sorted(books_dict.items(), key = operator.itemgetter(1)):
				print( book_title, ':' , value)


		elif user_word == '<titles>':
			print(book_titlelst)

		elif user_word in words_dict:
			# if user_word is in the dict as key
			# the count list
			WordCounts = words_dict[user_word]			
			# the dict for {book: counts}
			final_dict = {}
			for books in books_dict:
				try:
					 book_index = books_dict[books][0]
					 number_counts = WordCounts[book_index]
					 final_dict[books] = number_counts
				except:
					continue

			for booktitle, counts in sorted(final_dict.items(), key = operator.itemgetter(1), reverse=True):

				try:
					if counts > 1:
						print("The word {} appears {} times in {} (link: {})".format(user_word, counts, booktitle, books_dict[booktitle][1]))
					elif counts == 1:
						print("The word {} appears {} time in {} (link: {})".format(user_word, counts, booktitle, books_dict[booktitle][1]))

				except: 
					continue
		else: 
			print("'{}' does not exist in the word".format(user_word))

 





def main():

	match_dict() 

if __name__ == '__main__':
	main()












