# Do your imports
from bs4 import BeautifulSoup
import urllib.request as request

# Get the data from the server

html = request.urlopen("http://www.ischool.berkeley.edu/people/students/mims/2018")
content = html.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(content, 'html.parser')

# How many links are there?
links = soup.find_all('a')
len(links)

# Save all of the images on the site (use them to make The Facebook)

images = soup.find_all('img')
for i, img in enumerate(images):
    source = img['src'] # Get the src attribute from the img tag
    page = 'http://www.ischool.berkeley.edu/' + source # Combine the src into a full address
    request.urlretrieve(page, filename=str(i)+'.jpg') # Save the file


# But wait, that gave me every image on the site...how do I get only the faces??

# Only find the images classed as thumbnails
faces = soup.find_all('img', {'class': 'imagecache-profile-thumbnail'}) 
for i, img in enumerate(faces):
    source = img['src']
    page = 'http://www.ischool.berkeley.edu/' + source
    request.urlretrieve(page, filename=str(i)+'.jpg')

# Ok that was good, but what's going on with the file names? I want the files to show me who is in the photo

links = soup.find_all('a', {'class': 'imagecache-profile-thumbnail'})

for link in links:
    name = link['href'].split('/')[-1] # Last element in the src separated by /
    
    # Get the image contained in the link tag
    # We use find here instead of find_all because we want only the first result
    photo = link.find('img') 
    page = 'http://www.ischool.berkeley.edu/' + photo['src']
    request.urlretrieve(page, filename=name+'.jpg')






