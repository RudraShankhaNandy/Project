#importing selenium modules
import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#importing time libraries
from datetime import datetime
from time import sleep

#importing Beautiful Soup
from bs4 import BeautifulSoup as BS
import lxml

#importing requests module
import requests
import pandas as pd

#disabling notifications

#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--disable-notifications")
"""class FBextractor():
    
    def __init__(self,website,id,password):
        self.website = str(website)
        self.id = id
        self.password = str(password)
        self.content = []
        
    def login(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://mbasic.facebook.com/")
        sleep(2)
        self.username = driver.find_element('name','email')
        self.username.send_keys(self.id)
        self.passw = driver.find_element('name','pass')
        self.passw.send_keys(self.password)
        self.next_button = driver.find_element('name','login')
        self.next_button.click()
        self.driver.get(self.website)
        
    def extract_post_content(self):
        self.soup = BS(self.driver.page_source,"html.parser")
        self.all_posts = soup.find_all('div',{'class':'_55wo _56bf _5rgl'})
        for post in self.all_posts:
            info = {}
            comment = post.find('p').text
            self.content.append(comment)
        return self.content"""
            
            

driver = webdriver.Edge()

driver.get("https://mbasic.facebook.com/")
sleep(3)

username = driver.find_element('name','email')
username.send_keys("9903944177")

password = driver.find_element('name','pass')
password.send_keys("rudragamer123456")

next_button = driver.find_element('name','login')
next_button.click()

driver.get("https://mbasic.facebook.com/KolkataTrafficPolice?v=timeline&lst=100009394165274%3A100064619952245%3A1694067785&eav=AfYHfgiJARS5pC5VSIBWCE0cbjcms1Si_8FPKXvMSTSEG5zmrmhh5LUoDxNQYmZRCuE&paipv=0")

soup = BS(driver.page_source,"html.parser")
#incidents = driver.find_elements(By.XPATH,"//div[@class='x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z']]")
all_posts = soup.find_all('div',{'class':'_55wo _56bf _5rgl'})
for post in all_posts:
    info = {}
    content = post.find('p').text
        
all_links = soup.find_all('a')
for link in all_links:
    hype = link.find('span')
    if hype != None and hype.text == "See more stories":
        print(link)
print(all_links)
    