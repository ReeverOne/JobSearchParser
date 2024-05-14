import json
import requests
import re
from bs4 import BeautifulSoup

# Get users input on the string to search for in the domains on the list
searchstring = input('What word for I search for in the links? ')

# User Agent to use for scraping to get around 403 errors
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.2478.97"}

with open("domains.json") as fp:
    data = json.load(fp)

# GET the page based on url variable and extract the content via BS4
def pageData(url): # input variable of a url
    stock = requests.get(url, headers=headers) # request the content of the url using the headers string
    return BeautifulSoup(stock.content, 'lxml') # Create the soup from the stock content and parse it with an extractor. Using a non-standard parser 'lxml' for this. And return this result.

# Store the unique HREFs for each domain
finalresults = []

for domain in data:
    # Get the URL from the json
    url = domain.get('Domain')

    # Parse the page with lxml
    soup = pageData(url)

    # Find links that contain the string 'career' using Regular Expressions (RE)
    links = soup.find_all(href=re.compile(searchstring))

    # Store the uniqueurls until loop is complete
    uniqueurls = []

    # Clean up the URLs and make sure that each list item is unique
    for item in links:
        sendthis = item.get('href')
        if not sendthis.startswith('http'):
            sendthis = url + sendthis
        if sendthis not in uniqueurls:
            uniqueurls.append(sendthis)

    finalresults.append(uniqueurls)
    

print(finalresults)