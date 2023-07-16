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

#importing requests module
import pandas as pd

#disabling notifications

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options = chrome_options)
driver.get("https://facebook.com/login")
sleep(3)

username = driver.find_element(By.XPATH,"//input[@name='email']")
username.send_keys("--------")

password = driver.find_element(By.XPATH,"//input[@name='pass']")
password.send_keys("---------")

next_button = driver.find_element(By.XPATH,"//button[@name='login']")
next_button.click()

driver.get("https://facebook.com/KolkataTrafficPolice")