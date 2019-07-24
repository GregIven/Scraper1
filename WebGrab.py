"""To call from interpreter execfile('filename.py')"""


target_url = "https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&sc.keyword=&locT=C&locId=1132348&jobType="

from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

'''
browser = webdriver.Firefox()
browser.get(target_url)
innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
soup = BeautifulSoup(innerHTML)
elems = browser.find_elements_by_css_selector('.jl')
browser.implicitly_wait(10)
'''
True

def launch():
    global browser
    browser = webdriver.Firefox()
    #print("Input URL: ")


def close():
    browser.quit()

class WebHook:
    def get_url(self, url):
        self.url = url
        if not url.startswith('ht'):
                url = "https://www." + url
        print(url)
        browser.get(url)
        innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
        browser.implicitly_wait(5)
        self.innerHTML = innerHTML

    def get_element(elem):
        if 'class' in elem:
            #class_name =
            print('It is indeed')


    def apply_style(browser, elem):
        try:
            print("apply")
            browser.execute_script("arguments[0].setAttribute('style', 'border: 4px solid red');", elem)
        except Exception as e:
            print(e)
            pass
    ''''
    def find_Element():
        #this function will take the full html element find it by 1). Css 2). ID 3). XPATH

    '''

    '''
    def get_elem_info(browser, elem):
        try:
            title = browser.find_elements_by_css_selector('jobTitle')
    '''

    #Function to login
def facebook_login(browser):
    print("FB login tried")
    try:
        fb_button = browser.find_element_by_id("FbButton")
        #fb_button = browser.find_element(By.XPATH, "//div[@id='FbButton']") #IPATH example

        #This changes the current window handle
        window_before = browser.window_handles[0]
        fb_button.click()

        window_after = browser.window_handles[1]
        browser.switch_to_window(window_after)

        elem_user = browser.find_element_by_id('email')
        elem_pass = browser.find_element_by_id('pass')

        elem_user.send_keys('6506783895')
        elem_pass.send_keys('ffb420')

        browser.find_element_by_id('u_0_0').click()
    except Exception:
        pass
'''
for x in elems:
        apply_style(browser, x)
facebook_login()
'''
