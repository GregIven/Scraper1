"""To call from interpreter execfile('filename.py')"""

from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
url = "https://www.glassdoor.com/index.htm"
browser.get(url)

browser.implicitly_wait(10)

fb_button = browser.find_element_by_id("FbButton")
#Didnt work
#fb_button.click()
#Did work
fb_button = browser.find_element(By.XPATH, "//div[@id='FbButton']")


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


"""
Use to highlight element selected
elem = 'insert element here'

def apply_style(s):
        browser.execute_script("arguments[0].setAttribute('style', arguments[1])", elem, s)

orignal_style = elem.get_attribute('style')
apply_style("border: 4px solid red")
"""
