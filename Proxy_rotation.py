#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import pandas as pd 

from itertools import cycle
import traceback

def get_proxies():
    
    """
    This function will get free proxies from https://free-proxy-list.net/
    
    Returns
    -------
    IP_list: list of str proxies that are filtered as Elite Proxy & Https (ex:'176.56.107.224:35371')
    
    Examples
    --------
    ['103.108.98.1:55207','90.188.41.236:3128']
    
    """
    
    resp = requests.get('https://free-proxy-list.net/') 
    df = pd.read_html(resp.text)[0]
    df = df[:-1]
    df['IP Address'] = df['IP Address'].astype(str) 
    df["Port"] = [str(int(float(x))) for x in list(df.Port)]
    df['IP_Final'] = df['IP Address'].str.cat(df['Port'],sep=":")
    df = df[(df['Anonymity'] == 'elite proxy') & (df['Https'] == 'yes')]
    IP_list = list(df.IP_Final)
    
    return IP_list




