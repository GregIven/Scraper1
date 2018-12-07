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

#get the text of a <p> tag

p_one[10].contents #this gives the text as a list

#turn soup object contents into string

p_string = str(p_one)

#Idea for getting track lists, albums and artists from spotify... Look for id contains 'tracklist'


#Using selenium to get elements
from selenium import webdriver
driver = webdriver.Chrome() #this is for chrome browser
heading = driver.find_element_by_class_name('class name here')
#If list have to print in for loop
if type(heading) == lists:
    for head in heading:
        print(head.text.strip())
