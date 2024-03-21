#importing selenium modules
import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
#importing time libraries
from datetime import datetime
from time import sleep

#importing Beautiful Soup
from bs4 import BeautifulSoup as BS

#importing requests module
import requests
import pandas as pd


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
            
            
#main
driver = webdriver.Edge()

driver.get("https://mbasic.facebook.com/")
sleep(3)

username = driver.find_element('name','email')
username.send_keys("_________")

password = driver.find_element('name','pass')
password.send_keys("__________")

next_button = driver.find_element('name','login')
next_button.click()

driver.get("https://mbasic.facebook.com/KolkataTrafficPolice?v=timeline&lst=100009394165274%3A100064619952245%3A1694067785&eav=AfYHfgiJARS5pC5VSIBWCE0cbjcms1Si_8FPKXvMSTSEG5zmrmhh5LUoDxNQYmZRCuE&paipv=0")

soup = BS(driver.page_source,"html.parser")

next_page = 'https://mbasic.facebook.com'

#since the div class changes wrt page, this code avoids its use
#all_text = soup.find_all('p')
#print(all_text)
#for text in all_text:
#    if text != "":
#        print(text.text)

data_set = {}
data_set["date"] = []
data_set["time"] = []
data_set["post"] = []

#for moving onto next page we need to get the link
all_links = soup.find_all('a')
for link in all_links:
    hype = link.find('span')
    if hype != None and hype.text == "See more stories":
        next_page += link['href']#string object

#identifying the text and the datetime from div section only
#all_sect = soup.find('div')
#for sect in all_sect:
#    texts = sect.find_all('p')
#    for text in texts:
#        if "Traffic update:-" in text:
#            print(text.text)
#print(all_sect)

#code to extract content from 1st page
all_posts = soup.find_all('div',{'class':'_55wo _56bf _5rgl'})
for post in all_posts: 
    if post.find('p') != None and "Traffic update:-" in post.find('p').text:
        content = post.find('p').text
        date_time = post.find('abbr')
        k = date_time.text.split(' at ')
        data_set["post"].append(content.strip)
        data_set["date"].append("Today")
        data_set['time'].append(k[0])
print(data_set)


def getinfo(next_page):
    driver.get(next_page)
    sleep(1)
    soup = BS(driver.page_source,"html.parser")
    all_links = soup.find_all('a')
    
    global data_set
    
    #code to extract content from posts other than page-1
    all_posts = soup.find_all('div',{'class':'bnbobp'})
    for post in all_posts: 
        if post.find('p') != None and "Traffic update:-" in post.find('p').text:
            content = post.find('p').text
            date_time = post.find('abbr')
            k = date_time.text.split(' at ')
            data_set["post"].append(content.strip)
            data_set["date"].append(k[0])
            data_set['time'].append(k[1])
    sleep(2)
    #code to get next page link 
    for link in all_links:
        hype = link.find('span')
        if hype != None and hype.text == "See more stories":
            next_page += link['href']#string object
            if data_set['date'][len(data_set['date'])-1]!="31 December 2020":
                getinfo(next_page)
getinfo(next_page)
