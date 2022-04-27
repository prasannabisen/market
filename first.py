#!/usr/bin/env python
# coding: utf-8

# In[17]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from tabulate import tabulate
import time
import os
from IPython.display import clear_output
from platform   import system as system_name  # Returns the system/OS name
from subprocess import call   as system_call  # Execute a shell command
import csv
import numpy as np
import pandas as pd
import datetime


# In[18]:


#create new browser
driver = webdriver.Chrome(executable_path='./chromedriver')


# In[19]:


driver.get('https://app.drift.trade/portfolio?authority=AAw935winL5j5mVyWqSYiGkue52S9BHpRPwX7DUhQxyr')


# In[20]:


def clear_screen():
    system_call('clear')


# In[21]:


time.sleep(15)
head = ["MARKET", "DIRECTION" ,"p&l", "ENTRY PRICE", "EST. EXIT PRICE" ]
val=list()
entry=list()
while(1):
    time.sleep(2)
    # classes = driver.find_element(by = By.XPATH, value= '//*[@id="userInfo"]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]/span[1]')
    direction = driver.find_element(by = By.XPATH, value= '//*[@id="userInfo"]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[2]').text
    token= driver.find_element(by = By.XPATH, value='//*[@id="userInfo"]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/button').text
    pl=driver.find_element(by = By.XPATH, value='//*[@id="userInfo"]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]/span[1]').text
    entryPrice= driver.find_element(by = By.XPATH, value='//*[@id="userInfo"]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[6]/button').text
    entry=[]
    entry.append(datetime.datetime.now())
    entry.append(token)
    entry.append(direction)
    entry.append(pl)
    entry.append(entryPrice)
    table = pd.DataFrame(val,columns=["TIME","MARKET", "DIRECTION" ,"pl", "ENTRYPRICE"])
    if(table.shape[0]== 0 or table.iloc[int(table.shape[0])-1].MARKET!=token or table.iloc[int(table.shape[0])-1].DIRECTION!=direction or table.iloc[int(table.shape[0])-1].pl!=pl or table.iloc[int(table.shape[0])-1].ENTRYPRICE!=entryPrice):
        time.sleep(2)
        val.append(entry)
        filename= "market.csv"
        clear_screen()
        clear_output(wait=True)
        table.append(entry)
        print(table)
        table.to_csv('file1.csv')

