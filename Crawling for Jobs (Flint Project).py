#!/usr/bin/env python
# coding: utf-8

# In[11]:


#STEP1: import and install all necessary libraries
import pandas as pd
import urllib
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import requests
import xlsxwriter
import csv


# In[13]:


# investigate the nature of irina to see if it is usable. *note that I made the file

type(irina)


# In[33]:


#import the csv file to be used in this dataframe

with open("Flint Names and Frequency.csv") as load_file:
    reader = csv.reader(load_file)
    data = [tuple(row) for row in reader]


# In[34]:


df = pd.DataFrame(data, columns =['Name', 'Mentions']) 


# In[35]:


df


# In[42]:


irina = df.sort_values(axis=0, by='Mentions', ascending=False)


# In[43]:


irina.head


# In[45]:


aracelie = irina.head(100)


# In[46]:


# my working dataframe right now is the top mentioned, 100 names (except stephen busch, for some reason)
aracelie


# In[50]:


aracelie.iat[1,0]


# In[2]:


#from stackoverflow Dec 21 '17, user: furas


import urllib
from bs4 import BeautifulSoup
import requests
import webbrowser

text = 'hello world'
text = urllib.parse.quote_plus(text)

url = 'https://google.com/search?q=' + text

response = requests.get(url)

#with open('output.html', 'wb') as f:
#    f.write(response.content)
#webbrowser.open('output.html')

soup = BeautifulSoup(response.text, 'lxml')
for g in soup.find_all(class_='g'):
    print(g.text)
    print('-----')


# In[4]:


# for all x in y, search [google/news] and import all data from first article,
# search this new database for job titles by matching strings to words in my work database
# lastly, print name x and p, (p in article and in worklist)


# In[ ]:




