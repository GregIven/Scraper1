#This is a project to open up a web page and scrape all the text from it

import requests
from bs4 import BeautifulSoup

r = requests.get('https://en.wikipedia.org/wiki/Wyoming') #insert URL of page to scrape here

soup_one = BeautifulSoup(r.text, 'html.parser')

#method two

html_content = r.content

soup_two = BeautifulSoup(html_content)

#find all <p> tags

p_one = soup_two.find_all('p')