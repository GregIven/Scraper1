#Imports
#Call from terminal with $ python Tracklist.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get('https://open.spotify.com/browse/featured')
wait = WebDriverWait(driver, 20)
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-black')))
element.click()

wait = WebDriverWait(driver, 20)
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-block')))
element.click()

wait = WebDriverWait(driver, 20)
driver.find_element_by_id("email").send_keys('6506783895')
driver.find_element_by_id("pass").send_keys('ffb420')
driver.find_element_by_id("loginbutton").click()

element = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Your Library']")))
element.click()

driver.find_element_by_xpath("//a[contains(@href,'/collection/tracks')]").click()
#button = driver.find_element_by_class_name('btn-white').click()
