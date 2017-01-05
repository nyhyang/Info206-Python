import sys
import urllib
import urllib.request as req;
import urllib.error as er;
import string
from bs4 import BeautifulSoup
import re
import operator



def preprocess_yelp_page(content):
    ''' Remove extra spaces between HTML tags. '''
    content = ''.join([line.strip() for line in content.split('\n')])
    return content

#################################################################################
# Example code to illustrate the use of preprocess_yelp_page
# You may change these four lines of code

# Get the data from the server
result_dict= {}
"""dic {restaurant : review}"""
for number in range(4):
	"""for going through the 4 pages of the total reviews"""
	page_result = str(number) + '0'

	url = 'http://www.yelp.com/search?find_desc=restaurants&find_loc=San%20Francisco%2C+CA&sortby=rating&start=' + page_result
	try: 
		content = req.urlopen(url).read().decode('utf-8')
	except URLError: 
		print('URL crashes')

	content = preprocess_yelp_page(content) # Now *content* is a string containing the first page of search results, ready for processing with BeautifulSoup
	# print(url)
	# Create a BeautifulSoup object
	soup = BeautifulSoup(content, 'html.parser')

	# Your code goes here
	restaurants = soup.find_all('li', {'class': 'regular-search-result'})
	for restaurant in restaurants:
		# use span.text to get only the text within the children div 
		restaurant_name = restaurant.find('a', {'class': 'biz-name'}).span.text	
		# print(restaurant)
		reviews = restaurant.find('span', {'class': 'review-count'}).text
		reviews = int(reviews.split()[0])

		# fill in to the dictionary
		result_dict[restaurant_name] = reviews
	

# print(result_dict)
# sort the dictionary by number of reviews, reverse to start with the most number
result = sorted(result_dict.items(), key=operator.itemgetter(1), reverse = True)
print(result)

# put the result in the file
with open('restaurants.nyhyang.txt', 'w') as fout:
	for restaurant_name, reviews in result:
		fout.write(restaurant_name + ", " + str(reviews)+ "\n")











