#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randint
from random import choice
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from itertools import cycle
import traceback

import requests
import pandas as pd

# Import py
from Proxy_rotation import get_proxies


# In[2]:


"""
Importing second part of the urls for the YouTube videos.
"""

choices = open('url.txt', 'r').read().split('\n')
choices


# In[19]:


"""

This part can be used to see how the proxies are called and checked if they work or not.
We added a break so it will stop at the first iteration when it finds a proxy. But you can skip that part if you want.

"""

# url = 'https://httpbin.org/ip'
# proxy_pool = get_proxies()
# for i in range(1,10):
#     #Get a proxy from the pool
#     proxy = choice(proxy_pool)
#     print("Request #%d"%i)
#     try:
#         response = requests.get(url,proxies={"http": proxy, "https": proxy})
#         print("Good proxy",proxy)
#         break
#     except:
#         print("Skipping. Connnection error")


# In[21]:


"""

This part will show how we use Selenium to access YouTube through chromedriver. This is just a short demo with a count of 5
but using a Linux machine, you can leave the code work all day.

We added some touch of human behaviour like clicking the screen, searching by video, closing pop ups etc.
Other features can be added like clicking in the middle of the video or others.
"""

# for i in range(5):
#     sleep(randint(1,3))
#     options= webdriver.ChromeOptions()
#     options.add_argument("start-maximized")
#     options.add_argument("disable-infobars")
#     options.add_argument("--disable-extensions")
    
#     #f you are using Linux
# #     driver = webdriver.Chrome(options=options)
#     #if you are using Windows
#     driver = webdriver.Chrome(options=options,executable_path="C:\Webdrivers\chromedriver.exe")
    
#     wait = WebDriverWait(driver, 3)
#     video = choice(choices)
#     driver.get('https://www.youtube.com/results?search_query={}'.format(str(video)))
#     presence = EC.presence_of_element_located
#     visible = EC.visibility_of_element_located

#     wait.until(visible((By.ID, "video-title")))
#     driver.find_element_by_id("video-title").click()
#     sleep(5)
#     try:
#         WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/ytd-app/ytd-popup-container/paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/a/paper-button/yt-formatted-string'))).click()
#         driver.switch_to.frame(0)
#         WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/c-wiz/div[2]/div/div/div/div/div[2]/form/div/span/span"))).click()
#     except:
#         try:
#             driver.switch_to.frame(0)
#             WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/c-wiz/div[2]/div/div/div/div/div[2]/form/div/span/span"))).click()
#             WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/ytd-app/ytd-popup-container/paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/a/paper-button/yt-formatted-string'))).click()
#         except:
#             pass
#     sleep(randint(5,10))
#     driver.quit()


# In[ ]:


"""
This part will combine both of the algorithms. We try to find a working proxy and using it in our Selenium part.

"""

url = 'https://httpbin.org/ip'
for j in range(5):
    proxy_pool = get_proxies()
    for i in range(1,5):
        #Get a proxy from the pool
        proxy = choice(proxy_pool)
        print("Request #%d"%i, proxy)
        try:
            response = requests.get(url,proxies={"http": proxy, "https": proxy})
            print("Good proxy",proxy)
            
            sleep(randint(1,3))
            options= webdriver.ChromeOptions()
            options.add_argument('--proxy-server=%s' % str(proxy))
#             driver = webdriver.Chrome(options=options)
            driver = webdriver.Chrome(options=options,executable_path="C:\Webdrivers\chromedriver.exe")
            wait = WebDriverWait(driver, 3)
            video = choice(choices)
            driver.get('https://www.youtube.com/results?search_query={}'.format(str(video)))
            presence = EC.presence_of_element_located
            visible = EC.visibility_of_element_located
            
            wait.until(visible((By.ID, "video-title")))
            driver.find_element_by_id("video-title").click()
                
            sleep(5)
            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/ytd-app/ytd-popup-container/paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/a/paper-button/yt-formatted-string'))).click()
                driver.switch_to.frame(0)
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/c-wiz/div[2]/div/div/div/div/div[2]/form/div/span/span"))).click()
            except:
                try:
                    driver.switch_to.frame(0)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/c-wiz/div[2]/div/div/div/div/div[2]/form/div/span/span"))).click()
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/ytd-app/ytd-popup-container/paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/a/paper-button/yt-formatted-string'))).click()
                except:
                    pass
            sleep(randint(5,10))
            driver.quit()
        except:
            print("Skipping. Connnection error")


# In[ ]:




