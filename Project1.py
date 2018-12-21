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


#Using selenium to get button element
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://open.spotify.com/browse/featured')

button = driver.find_element_by_class_name('btn-white')
button.click()

#getting tracklist find_element_by_class_name
tracklist = driver.find_element_by_class_name('tracklist-name').text

#Updated
