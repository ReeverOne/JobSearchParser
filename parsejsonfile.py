import json
import requests
import re
from bs4 import BeautifulSoup

# Get users input on the string to search for in the domains on the list
searchstring = 'career' # Switch to a user input before final revision

# User Agent to use for scraping to get around 403 errors
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.2478.97"}

# Load the json list of domains
with open("domains.json") as fp:
    data = json.load(fp)

# GET the page based on url variable and extract the content via BS4
def pageData(url): # input variable of a url
    stock = requests.get(url, headers=headers) # request the content of the url using the headers string
    return BeautifulSoup(stock.content, 'lxml') # Create the soup from the stock content and parse it with an extractor. Using a non-standard parser 'lxml' for this. And return this result.

# Store the unique HREFs for each domain
class finalresults:
    def __init__(self, name, urls):
        self.name = name
        self.urls = urls

# Loop through each domain and scan for links containing the searchstring
for domain in data:
    # Get the URL from the json
    url = domain.get('Domain') # Set URL
    company = domain.get('Company') # Set Company name

    # Parse the page with lxml
    soup = pageData(url)

    # Find links that contain the string 'career' using Regular Expressions (RE)
    links = soup.find_all(href=re.compile(searchstring))

    # Store the uniqueurls until loop is complete
    uniqueurls = {}
    
    listofurls = []

    # Clean up the URLs and make sure that each list item is unique
    for item in links:
        listofurls = []
        if not item.get('href').startswith('http'):
            updateto = url + item.get('href')
            listofurls.append(updateto)
        else:
            listofurls.append(item.get('href'))
"""            
    # Compile the data into an array
    uniqueurls = json.loads('{"Company": "' + company + '", "URLs": [' + listofurls + ']}')
    
    # Add the array to the final results variable
    finalresults = finalresults + uniqueurls
        
        
        getcompany = '"Company": "' + company
        jdata = '{' + getcompany + '", "URL": "' + item.get('href') + '"}'
        sendthis = json.loads(jdata)
        if not sendthis['URL'].startswith('http'):
            updateto = url + sendthis['URL']
            sendthis['URL'] = updateto
        if sendthis['URL'] not in uniqueurls:
            uniqueurls.update(sendthis)

    # Add the results for the specific domain searched in the final variable
    finalresults.update(uniqueurls)
    

print(finalresults)
"""