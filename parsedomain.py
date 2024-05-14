import requests
import re
from bs4 import BeautifulSoup

# URL to lookup
url = "https://theedigital.com"

# Search string on the page
searchstring = 'career'

# User Agent to use for scraping to get around 403 errors
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.2478.97"}

# GET the page based on url variable and extract the content via BS4
def pageData(url): # input variable of a url
    stock = requests.get(url, headers=headers) # request the content of the url using the headers string
    soup = BeautifulSoup(stock.content, 'lxml') # Create the soup from the stock content and parse it with an extractor. Using a non-standard parser 'lxml' for this.
    return soup # return the content

# Parse the page with lxml
soup = pageData(url)

# Find links that contain the string 'career' using Regular Expressions (RE)
career_links = soup.find_all(href=re.compile(searchstring))

uniqueurls = []

for item in career_links:
    sendthis = item.get('href')
    if not sendthis.startswith('http'):
        sendthis = url + sendthis
    if sendthis not in uniqueurls:
        uniqueurls.append(sendthis)

print(uniqueurls)


"""
# Clean up the URLs and make sure that each list item is unique
for uniquelist in career_links:
    thislist = uniquelist.get('href')
    uniquelist = []
    if thislist not in uniquelist:
        uniquelist.append(thislist)

# Print the result
print(uniquelist)

for row in career_links:
    if row.get('href').startswith('http'):
        thislist = row.get('href')
    else:
        thislist = url + row.get('href')
"""    