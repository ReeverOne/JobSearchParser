import requests
import re
from bs4 import BeautifulSoup

# URL to lookup
url = "https://www.google.com"

# Search string on the page
jobsearchstring = 'career'

# User Agent to use for scraping
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.2478.97"}

# GET the page
# response = requests.get(url, headers=headers)

# GET the page based on url variable and extract the content via BS4
def pageData(url): # input variable of a url
    stock = requests.get(url, headers=headers) # request the content of the url using the headers string
    soup = BeautifulSoup(stock.content, 'lxml') # Create the soup from the stock content and parse it with an extractor. Using a non-standard parser 'lxml' for this.
    return soup # return the content

# Parse the page with lxml
soup = pageData(url)

# Find links that contain the string 'career' using Regular Expressions (RE)
career_links = soup.find_all(href=re.compile(jobsearchstring))

for uniquelist in career_links:
    thislist = uniquelist.get('href')
    uniquelist = []
    if thislist not in uniquelist:
        uniquelist.append(thislist)
    
print(uniquelist)

