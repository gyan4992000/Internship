#!/usr/bin/env python
# coding: utf-8

# # Ques1: Write a python program to display all the header tags from wikipedia.org.

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


page=requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[3]:


page


# In[4]:


soup=BeautifulSoup(page.content)
soup


# In[7]:


titles =[]

for i in soup.find_all('h2', class_="mp-h2"):
    titles.append(i.text)

titles


# # Ques2: Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release) and make data frame.

# In[8]:


from bs4 import BeautifulSoup
import requests


# In[9]:


page_1=requests.get('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&ref_=adv_prv')


# In[10]:


page_1


# In[11]:


soup_1=BeautifulSoup(page_1.content)
soup_1


# In[12]:


#Importing names of first 50 IMDB rating movies available on Page 1

movies_name=[]

for i in soup_1.find_all('h3', class_="lister-item-header"):
    movies_name.append(i.text.split(sep='\n'))
    
movies_name


# In[13]:


ratings=[]

for i in soup_1.find_all('div', class_="inline-block ratings-imdb-rating"):
    ratings.append(i.text.split()[0])
    
ratings


# In[14]:


#Year of Release Page 1

yor=[]

for i in soup_1.find_all('span', class_="lister-item-year text-muted unbold"):
    yor.append(i.text)

yor


# Page 2

# In[15]:


page_2=requests.get('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&start=51&ref_=adv_nxt')
page_2


# In[16]:


soup_2=BeautifulSoup(page_2.content)
soup_2


# In[17]:


for i in soup_2.find_all('h3', class_="lister-item-header"):
    movies_name.append(i.text.split(sep='\n'))
    
movies_name


# In[18]:


#Ratings Page 2

for i in soup_2.find_all('div', class_="inline-block ratings-imdb-rating"):
    ratings.append(i.text.split()[0])
    
ratings


# In[19]:


#Year of Release Page 2

for i in soup_2.find_all('span', class_="lister-item-year text-muted unbold"):
    yor.append(i.text)

yor


# In[20]:


#Checking length
print(len(movies_name),len(ratings), len(yor))


# In[21]:


#Creating DataFrame

import pandas as pd

imdb = pd.DataFrame({'Names': movies_name,'IMDB Ratings':ratings, 'Year of Release': yor})
imdb


# # Ques3: Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of release) and make data frame.

# In[22]:


from bs4 import BeautifulSoup
import requests


# In[23]:


page=requests.get('https://www.imdb.com/india/top-rated-indian-movies')


# In[24]:


soup=BeautifulSoup(page.content)
soup


# In[25]:


n=100
movies_name=[] * n

for i in soup.find_all('td', class_="titleColumn"):
    movies_name.append(i.text.split(sep='\n')) 
    
for i in range (0,100):
    print(movies_name[i])


# In[26]:


ratings=[]

for i in soup.find_all('td', class_="ratingColumn imdbRating"):
    ratings.append(i.text.split()[0])
    
ratings


# In[27]:


#Year of Release

yor=[]

for i in soup.find_all('span', class_="secondaryInfo"):
    yor.append(i.text)

yor


# In[28]:


#Checking length
print(len(movies_name),len(ratings), len(yor))


# In[29]:


#Creating DataFrame

import pandas as pd

imdb = pd.DataFrame({'Names': movies_name,'IMDB Ratings':ratings, 'Year of Release': yor})
imdb


# # Ques 4: Write s python program to display list of respected former presidents of India(i.e. Name , Term of office) from https://presidentofindia.nic.in/former-presidents.htm

# In[30]:


from bs4 import BeautifulSoup
import requests


# In[31]:


page=requests.get('https://presidentofindia.nic.in/former-presidents.htm')
page


# In[32]:


soup=BeautifulSoup(page.content)
soup


# In[33]:


names=[]

for i in soup.find_all('div', class_="presidentListing"):
    names.append(i.text.split(sep='\n')[1]) 
    
names


# In[34]:


term=[]

for i in soup.find_all('div', class_="presidentListing"):
    term.append(i.text.split(sep='\n')[2]) 
    
term


# In[35]:


#Checking length
print(len(names),len(term))


# In[36]:


#Creating DataFrame

import pandas as pd

india = pd.DataFrame({'President Name': names,'Term':term})
india


# # Ques 7: Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world :
# ## i) Headline
# ## ii) Time
# ## iii) News Link

# In[37]:


from bs4 import BeautifulSoup
import requests


# In[38]:


page=requests.get('https://www.cnbc.com/world/?region=world')


# In[39]:


page


# In[40]:


soup=BeautifulSoup(page.content, 'html.parser')
soup


# In[41]:


headline=[]

for i in soup.find_all('div', class_="LatestNews-headlineWrapper"):
    headline.append(i.text.split(sep='Ago')[1]) 
    
headline


# In[42]:


time=[]

for i in soup.find_all('div', class_="LatestNews-headlineWrapper"):
    time.append(i.text.split(sep='Ago')[0]) 
    
time


# In[43]:


headline_link=[]

for link in soup.find_all('a', class_="LatestNews-headline"):
    headline_link.append(link.get('href')) 


# In[44]:


#Creating DataFrame

import pandas as pd

news = pd.DataFrame({'Headline': headline,'Time':time, 'Link': headline_link})
news


# # Ques 8:  Write a python program to scrape the details of most downloaded articles from AI in last 90 days. 
# ## https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
# ## Scrape below mentioned details :
# ## i) Paper Title 
# ## ii) Authors
# ## iii) Published Date 
# ## iv) Paper URL

# In[45]:


from bs4 import BeautifulSoup
import requests


# In[46]:


page=requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')


# In[47]:


page


# In[48]:


soup=BeautifulSoup(page.content, 'html.parser')
soup


# In[49]:


title=[]

for i in soup.find_all('h2', class_="sc-1qrq3sd-1 MKjKb sc-1nmom32-0 sc-1nmom32-1 hqhUYH ebTA-dR"):
    title.append(i.text) 
    
title


# In[50]:


author=[]

for i in soup.find_all('span', class_="sc-1w3fpd7-0 pgLAT"):
    author.append(i.text) 
    
author


# In[51]:


released=[]

for i in soup.find_all('span', class_="sc-1thf9ly-2 bKddwo"):
    released.append(i.text) 
    
released


# In[52]:


url = []

for link in soup.find_all('a', class_="sc-5smygv-0 nrDZj"):
    url.append(link.get('href'))


# In[53]:


print(len(title),len(author), len(released),len(url))


# In[54]:


#Creating DataFrame

import pandas as pd

AI = pd.DataFrame({'Title': title,'Author':author,'Published Date':released,'URL':url})
AI


# # Ques 9: Write a python program to scrape mentioned details from dineout.co.in :
# ## i) Restaurant name
# ## ii) Cuisine
# ## iii) Location 
# ## iv) Ratings
# ## v) Image URL

# In[55]:


from bs4 import BeautifulSoup
import requests


# In[56]:


page=requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')


# In[57]:


page


# In[58]:


soup=BeautifulSoup(page.content, 'html.parser')
soup


# In[59]:


restaurant_name=[]

for i in soup.find_all('a', class_="restnt-name ellipsis"):
    restaurant_name.append(i.text) 
    
restaurant_name


# In[60]:


cuisine=[]

for i in soup.find_all('span', class_="double-line-ellipsis"):
    cuisine.append(i.text.split(sep='|')[1]) 
    
cuisine


# In[61]:


loc=[]

for i in soup.find_all('div', class_="restnt-loc ellipsis"):
    loc.append(i.text) 
    
loc


# In[62]:


ratings=[]
for i in soup.find_all('div', class_="restnt-rating rating-4"):
    ratings.append(i.text) 
    
ratings


# In[66]:


img_url=[]

for i in soup.find_all('img',class_="no-img"):
    img_url.append(i['data-src'])
    
img_url


# In[67]:


#Creating DataFrame

import pandas as pd

dineout = pd.DataFrame({'Restaurant name': restaurant_name,'Cuisine': cuisine, 'Location ': loc, 'Ratings': ratings, 'Image URL': img_url})
dineout


# # Ques 10: Write a python program to scrape the details of top publications from Google Scholar from https://scholar.google.com/citations?view_op=top_venues&hl=en
# ## i) Rank 
# ## ii) Publication
# ## iii) h5-index
# ## iv) h5-median

# In[68]:


from bs4 import BeautifulSoup
import requests


# In[69]:


page=requests.get('https://scholar.google.com/citations?view_op=top_venues&hl=en')
page


# In[70]:


soup=BeautifulSoup(page.content, 'html.parser')
soup


# In[71]:


rank=[]
for i in soup.find_all('td', class_="gsc_mvt_p"):
    rank.append(i.text) 
    
rank


# In[72]:


publication=[]
for i in soup.find_all('td', class_="gsc_mvt_t"):
    publication.append(i.text) 
    
publication


# In[73]:


h5i=[]
for i in soup.find_all('a', class_="gs_ibl gsc_mp_anchor"):
    h5i.append(i.text.split()) 
    
h5i


# In[74]:


h5m=[]
for i in soup.find_all('span', class_="gs_ibl gsc_mp_anchor"):
    h5m.append(i.text) 
    
h5m


# In[75]:


print(len(rank),len(publication),len(h5i),len(h5m))


# In[76]:


#Creating DataFrame

import pandas as pd

top_pub = pd.DataFrame({'Rank': rank,'Publication':publication, ' H5-index': h5i, ' H5-median': h5m})
top_pub


# In[ ]:




