#!/usr/bin/env python
# coding: utf-8

# # Ques1: Write a python program to display all the header tags from wikipedia.org.

# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page=requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[4]:


page


# In[5]:


soup=BeautifulSoup(page.content)
soup


# In[6]:


titles =[]

for i in soup.find_all('h2', class_="mp-h2"):
    titles.append(i.text)

titles


# # Ques2: Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release) and make data frame.

# In[7]:


from bs4 import BeautifulSoup
import requests


# In[8]:


page_1=requests.get('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&ref_=adv_prv')


# In[9]:


page_1


# In[10]:


soup_1=BeautifulSoup(page_1.content)
soup_1


# In[11]:


#Importing names of first 50 IMDB rating movies available on Page 1

movies_name=[]

for i in soup_1.find_all('h3', class_="lister-item-header"):
    movies_name.append(i.text.split(sep='\n'))
    
movies_name


# In[12]:


ratings=[]

for i in soup_1.find_all('div', class_="inline-block ratings-imdb-rating"):
    ratings.append(i.text.split()[0])
    
ratings


# In[13]:


#Year of Release Page 1

yor=[]

for i in soup_1.find_all('span', class_="lister-item-year text-muted unbold"):
    yor.append(i.text)

yor


# Page 2

# In[14]:


page_2=requests.get('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&start=51&ref_=adv_nxt')
page_2


# In[15]:


soup_2=BeautifulSoup(page_2.content)
soup_2


# In[16]:


for i in soup_2.find_all('h3', class_="lister-item-header"):
    movies_name.append(i.text.split(sep='\n'))
    
movies_name


# In[17]:


#Ratings Page 2

for i in soup_2.find_all('div', class_="inline-block ratings-imdb-rating"):
    ratings.append(i.text.split()[0])
    
ratings


# In[18]:


#Year of Release Page 2

for i in soup_2.find_all('span', class_="lister-item-year text-muted unbold"):
    yor.append(i.text)

yor


# In[19]:


#Checking length
print(len(movies_name),len(ratings), len(yor))


# In[20]:


#Creating DataFrame

import pandas as pd

imdb = pd.DataFrame({'Names': movies_name,'IMDB Ratings':ratings, 'Year of Release': yor})
imdb


# # Ques3: Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of release) and make data frame.

# In[21]:


from bs4 import BeautifulSoup
import requests


# In[24]:


page=requests.get('https://www.imdb.com/india/top-rated-indian-movies')


# In[25]:


soup=BeautifulSoup(page.content)
soup


# In[26]:


n=100
movies_name=[] * n

for i in soup.find_all('td', class_="titleColumn"):
    movies_name.append(i.text.split(sep='\n')) 
names_list=movies_name[0:100]
names_list


# In[27]:


ratings=[]

for i in soup.find_all('td', class_="ratingColumn imdbRating"):
    ratings.append(i.text.split()[0])
    
final_ratings=ratings[0:100]
final_ratings


# In[28]:


#Year of Release

yor=[]

for i in soup.find_all('span', class_="secondaryInfo"):
    yor.append(i.text)

year=yor[0:100]
year


# In[29]:


#Checking length
print(len(names_list),len(final_ratings), len(year))


# In[30]:


#Creating DataFrame

import pandas as pd

imdb = pd.DataFrame({'Names': names_list,'IMDB Ratings':final_ratings, 'Year of Release': year})
imdb


# # Ques 4: Write s python program to display list of respected former presidents of India(i.e. Name , Term of office) from https://presidentofindia.nic.in/former-presidents.htm

# In[31]:


from bs4 import BeautifulSoup
import requests


# In[32]:


page=requests.get('https://presidentofindia.nic.in/former-presidents.htm')
page


# In[33]:


soup=BeautifulSoup(page.content)
soup


# In[34]:


names=[]

for i in soup.find_all('div', class_="presidentListing"):
    names.append(i.text.split(sep='\n')[1]) 
    
names


# In[35]:


term=[]

for i in soup.find_all('div', class_="presidentListing"):
    term.append(i.text.split(sep='\n')[2]) 
    
term


# In[36]:


#Checking length
print(len(names),len(term))


# In[37]:


#Creating DataFrame

import pandas as pd

india = pd.DataFrame({'President Name': names,'Term':term})
india


# # Ques 5: Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:

# # A. Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.

# In[38]:


from bs4 import BeautifulSoup
import requests


# In[39]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
page


# In[40]:


soup=BeautifulSoup(page.content)
soup


# In[41]:


country=[]

for i in soup.find_all('span', class_="u-hide-phablet"):
        country.append(i.text) 

team=country[0:10]
team


# In[42]:


first_team_match=[]

for i in soup.find_all('td', class_="rankings-block__banner--matches"):
        first_team_match.append(i.text) 

first_team_match


# In[43]:


matches=[]
for i in soup.find_all('td', class_="table-body__cell u-center-text"):
        matches.append(i.text) 

matches


# In[44]:


list1=[]
for i in range(0,38,2):
    list1.append(matches[i])
list1


# In[45]:


#Adding first element in the list
list1=first_team_match+list1
list1=list1[0:10]
list1


# In[46]:


#Points
points=[]
for i in range(1,39,2):
    points.append(matches[i])
points


# In[47]:


#adding first team points in the list
first_team_point=[]

for i in soup.find_all('td', class_="rankings-block__banner--points"):
        first_team_point.append(i.text) 

first_team_point


# In[48]:


points=first_team_point+points
points=points[0:10]
points


# In[49]:


#Ratings
first_team_ratings=[]

for i in soup.find_all('td', class_="rankings-block__banner--rating u-text-right"):
        first_team_ratings.append(i.text.split())
first_team_ratings


# In[50]:


ratings=[]
for i in soup.find_all('td', class_="table-body__cell u-text-right rating"):
        ratings.append(i.text)
ratings


# In[51]:


ratings=first_team_ratings+ratings
ratings=ratings[0:10]
ratings


# In[52]:


#Creating dataframe

import pandas as pd

odi_teams = pd.DataFrame({'Country': team,'Matches':list1,'Points':points,'Ratings':ratings})
odi_teams


# # B) Top 10 ODI Batsmen along with the records of their team and rating.

# In[53]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi')
page


# In[54]:


soup=BeautifulSoup(page.content)
soup


# In[55]:


#adding first player name in the list
first_player_name=[]

for i in soup.find_all('div', class_="rankings-block__banner--name"):
        first_player_name.append(i.text) 

first_player_name=first_player_name[0:1]
first_player_name


# In[56]:


players=[]
for i in soup.find_all('td', class_="table-body__cell name"):
        players.append(i.text.split()) 

players=players[0:9]
players


# In[57]:


players=first_player_name+players
players


# In[58]:


first_player_nationality=[]
for i in soup.find_all('div', class_="rankings-block__banner--nationality"):
        first_player_nationality.append(i.text.split()[0]) 

first_player_nationality=first_player_nationality[0:1]
first_player_nationality


# In[59]:


nationality=[]
for i in soup.find_all('span', class_="table-body__logo-text"):
        nationality.append(i.text) 

nationality=nationality[0:9]
nationality


# In[60]:


nationality=first_player_nationality+nationality
nationality


# In[61]:


first_player_ratings=[]
for i in soup.find_all('div', class_="rankings-block__banner--nationality"):
        first_player_ratings.append(i.text.split()[1]) 

first_player_ratings=first_player_ratings[0:1]
first_player_ratings


# In[62]:


ratings=[]
for i in soup.find_all('td', class_="table-body__cell u-text-right rating"):
        ratings.append(i.text) 

ratings=ratings[0:9]
ratings


# In[63]:


ratings=first_player_ratings+ratings
ratings


# In[64]:


#Creating dataframe

import pandas as pd

odi_batsmen = pd.DataFrame({'Player': players,'Team':nationality,'Ratings':ratings})
odi_batsmen


# # C) Top 10 ODI bowlers along with the records of their team and rating.

# In[65]:


#adding first bowler name in the list
first_bowler_name=[]

for i in soup.find_all('div', class_="rankings-block__banner--name"):
        first_bowler_name.append(i.text) 

first_bowler_name=first_bowler_name[1:2]
first_bowler_name


# In[66]:


bowlers=[]
for i in soup.find_all('td', class_="table-body__cell name"):
        bowlers.append(i.text) 

bowlers=bowlers[9:18]
bowlers


# In[67]:


bowlers=first_bowler_name+bowlers
bowlers


# In[68]:


first_bowler_nationality=[]
for i in soup.find_all('div', class_="rankings-block__banner--nationality"):
        first_bowler_nationality.append(i.text.split()[0]) 

first_bowler_nationality=first_bowler_nationality[1:2]
first_bowler_nationality


# In[69]:


nationality=[]
for i in soup.find_all('span', class_="table-body__logo-text"):
        nationality.append(i.text) 

nationality=nationality[9:18]
nationality


# In[70]:


nationality=first_bowler_nationality+nationality
nationality


# In[71]:


first_bowler_ratings=[]
for i in soup.find_all('div', class_="rankings-block__banner--nationality"):
        first_bowler_ratings.append(i.text.split()[1]) 

first_bowler_ratings=first_bowler_ratings[1:2]
first_bowler_ratings


# In[72]:


bowlers_ratings=[]
for i in soup.find_all('td', class_="table-body__cell u-text-right rating"):
        bowlers_ratings.append(i.text) 

bowlers_ratings=bowlers_ratings[9:18]
bowlers_ratings


# In[73]:


bowlers_ratings=first_bowler_ratings+bowlers_ratings
bowlers_ratings


# In[74]:


print(len(bowlers),len(nationality),len(bowlers_ratings))


# In[75]:


#Creating dataframe

import pandas as pd

odi_bowlers = pd.DataFrame({'Player': bowlers,'Nationality':nationality,'Ratings':bowlers_ratings})
odi_bowlers


# # Ques 6: Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:

# # A. Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.

# In[76]:


from bs4 import BeautifulSoup
import requests


# In[77]:


page=requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
page


# In[78]:


soup=BeautifulSoup(page.content)
soup


# In[79]:


country=[]

for i in soup.find_all('span', class_="u-hide-phablet"):
        country.append(i.text) 

team=country[0:10]
team


# In[80]:


first_team_match=[]

for i in soup.find_all('td', class_="rankings-block__banner--matches"):
        first_team_match.append(i.text) 

first_team_match


# In[81]:


matches=[]
for i in soup.find_all('td', class_="table-body__cell u-center-text"):
        matches.append(i.text) 

matches


# In[82]:


print(len(matches))


# In[83]:


list1=[]
for i in range(0,18,2):
    list1.append(matches[i])
list1


# In[84]:


list1=first_team_match+list1
list1=list1[0:10]
list1


# In[85]:


#Points
points=[]
for i in range(1,19,2):
    points.append(matches[i])
points


# In[86]:


#adding first team points in the list
first_team_point=[]

for i in soup.find_all('td', class_="rankings-block__banner--points"):
        first_team_point.append(i.text) 

first_team_point


# In[87]:


points=first_team_point+points
points=points[0:10]
points


# In[88]:


#Ratings
first_team_ratings=[]

for i in soup.find_all('td', class_="rankings-block__banner--rating u-text-right"):
        first_team_ratings.append(i.text.split())
first_team_ratings


# In[89]:


ratings=[]
for i in soup.find_all('td', class_="table-body__cell u-text-right rating"):
        ratings.append(i.text)
ratings


# In[90]:


ratings=first_team_ratings+ratings
ratings=ratings[0:10]
ratings


# In[91]:


print(len(team),len(list1),len(points),len(ratings))


# In[92]:


#Creating dataframe

import pandas as pd

odi_womens_teams = pd.DataFrame({'Country': team,'Matches':list1,'Points':points,'Ratings':ratings})
odi_womens_teams


# # B) Top 10 women’s ODI Batting players along with the records of their team and rating.

# In[93]:


page=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi')
page


# In[94]:


soup=BeautifulSoup(page.content)
soup


# In[95]:


#adding first player name in the list
first_player_name=[]

for i in soup.find_all('div', class_="rankings-block__banner--name"):
        first_player_name.append(i.text) 

first_player_name=first_player_name[0:1]
first_player_name


# In[96]:


players=[]
for i in soup.find_all('td', class_="table-body__cell name"):
        players.append(i.text.split()) 

players=players[0:9]
players


# In[97]:


players=first_player_name+players
players


# In[98]:


first_player_nationality=[]
for i in soup.find_all('div', class_="rankings-block__banner--nationality"):
        first_player_nationality.append(i.text.split()[0]) 

first_player_nationality=first_player_nationality[0:1]
first_player_nationality


# In[99]:


nationality=[]
for i in soup.find_all('span', class_="table-body__logo-text"):
        nationality.append(i.text) 

nationality=nationality[0:9]
nationality


# In[100]:


nationality=first_player_nationality+nationality
nationality


# In[101]:


first_player_ratings=[]
for i in soup.find_all('div', class_="rankings-block__banner--nationality"):
        first_player_ratings.append(i.text.split()[1]) 

first_player_ratings=first_player_ratings[0:1]
first_player_ratings


# In[102]:


ratings=[]
for i in soup.find_all('td', class_="table-body__cell u-text-right rating"):
        ratings.append(i.text) 

ratings=ratings[0:9]
ratings


# In[103]:


ratings=first_player_ratings+ratings
ratings


# In[104]:


#Creating dataframe

import pandas as pd

odi_women_batting = pd.DataFrame({'Player': players,'Team':nationality,'Ratings':ratings})
odi_women_batting


# # C) Top 10 women’s ODI all-rounder along with the records of their team and rating.

# In[105]:


#adding first bowler name in the list
first_allrounder_name=[]

for i in soup.find_all('div', class_="rankings-block__banner--name"):
        first_allrounder_name.append(i.text) 

first_allrounder_name=first_allrounder_name[2:3]
first_allrounder_name


# In[106]:


allrounders=[]
for i in soup.find_all('td', class_="table-body__cell name"):
        allrounders.append(i.text) 

allrounders=allrounders[18:27]
allrounders


# In[107]:


allrounders=first_allrounder_name+allrounders
allrounders


# In[108]:


first_allrounder_nationality=[]
for i in soup.find_all('div', class_="rankings-block__banner--nationality"):
        first_allrounder_nationality.append(i.text.split()[0]) 

first_allrounder_nationality=first_allrounder_nationality[2:3]
first_allrounder_nationality


# In[109]:


nationality=[]
for i in soup.find_all('span', class_="table-body__logo-text"):
        nationality.append(i.text) 

nationality=nationality[18:27]
nationality


# In[110]:


nationality=first_allrounder_nationality+nationality
nationality


# In[111]:


first_allrounder_ratings=[]
for i in soup.find_all('div', class_="rankings-block__banner--nationality"):
        first_allrounder_ratings.append(i.text.split()[1]) 

first_allrounder_ratings=first_allrounder_ratings[2:3]
first_allrounder_ratings


# In[112]:


ratings=[]
for i in soup.find_all('td', class_="table-body__cell u-text-right rating"):
        ratings.append(i.text) 

ratings=ratings[18:27]
ratings


# In[113]:


ratings=first_allrounder_ratings+ratings
ratings


# In[114]:


print(len(allrounders),len(nationality),len(ratings))


# In[115]:


#Creating dataframe

import pandas as pd

odi_allrounders = pd.DataFrame({'Player': allrounders,'Team':nationality,'Ratings':ratings})
odi_allrounders


# # Ques 7: Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world :
# ## i) Headline
# ## ii) Time
# ## iii) News Link

# In[116]:


from bs4 import BeautifulSoup
import requests


# In[117]:


page=requests.get('https://www.cnbc.com/world/?region=world')


# In[118]:


page


# In[119]:


soup=BeautifulSoup(page.content, 'html.parser')
soup


# In[120]:


headline=[]

for i in soup.find_all('div', class_="LatestNews-headlineWrapper"):
    headline.append(i.text.split(sep='Ago')[1]) 
    
headline


# In[121]:


time=[]

for i in soup.find_all('div', class_="LatestNews-headlineWrapper"):
    time.append(i.text.split(sep='Ago')[0]) 
    
time


# In[122]:


headline_link=[]

for link in soup.find_all('a', class_="LatestNews-headline"):
    headline_link.append(link.get('href')) 


# In[123]:


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

# In[124]:


from bs4 import BeautifulSoup
import requests


# In[125]:


page=requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')


# In[126]:


page


# In[127]:


soup=BeautifulSoup(page.content, 'html.parser')
soup


# In[128]:


title=[]

for i in soup.find_all('h2', class_="sc-1qrq3sd-1 MKjKb sc-1nmom32-0 sc-1nmom32-1 hqhUYH ebTA-dR"):
    title.append(i.text) 
    
title


# In[129]:


author=[]

for i in soup.find_all('span', class_="sc-1w3fpd7-0 pgLAT"):
    author.append(i.text) 
    
author


# In[130]:


released=[]

for i in soup.find_all('span', class_="sc-1thf9ly-2 bKddwo"):
    released.append(i.text) 
    
released


# In[131]:


url = []

for link in soup.find_all('a', class_="sc-5smygv-0 nrDZj"):
    url.append(link.get('href'))


# In[132]:


print(len(title),len(author), len(released),len(url))


# In[133]:


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

# In[134]:


from bs4 import BeautifulSoup
import requests


# In[135]:


page=requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')


# In[136]:


page


# In[137]:


soup=BeautifulSoup(page.content, 'html.parser')
soup


# In[138]:


restaurant_name=[]

for i in soup.find_all('a', class_="restnt-name ellipsis"):
    restaurant_name.append(i.text) 
    
restaurant_name


# In[139]:


cuisine=[]

for i in soup.find_all('span', class_="double-line-ellipsis"):
    cuisine.append(i.text.split(sep='|')[1]) 
    
cuisine


# In[140]:


loc=[]

for i in soup.find_all('div', class_="restnt-loc ellipsis"):
    loc.append(i.text) 
    
loc


# In[141]:


ratings=[]
for i in soup.find_all('div', class_="restnt-rating rating-4"):
    ratings.append(i.text) 
    
ratings


# In[142]:


img_url=[]

for i in soup.find_all('img',class_="no-img"):
    img_url.append(i['data-src'])
    
img_url


# In[143]:


#Creating DataFrame

import pandas as pd

dineout = pd.DataFrame({'Restaurant name': restaurant_name,'Cuisine': cuisine, 'Location ': loc, 'Ratings': ratings, 'Image URL': img_url})
dineout


# # Ques 10: Write a python program to scrape the details of top publications from Google Scholar from https://scholar.google.com/citations?view_op=top_venues&hl=en
# ## i) Rank 
# ## ii) Publication
# ## iii) h5-index
# ## iv) h5-median

# In[144]:


from bs4 import BeautifulSoup
import requests


# In[145]:


page=requests.get('https://scholar.google.com/citations?view_op=top_venues&hl=en')
page


# In[146]:


soup=BeautifulSoup(page.content, 'html.parser')
soup


# In[147]:


rank=[]
for i in soup.find_all('td', class_="gsc_mvt_p"):
    rank.append(i.text) 
    
rank


# In[148]:


publication=[]
for i in soup.find_all('td', class_="gsc_mvt_t"):
    publication.append(i.text) 
    
publication


# In[149]:


h5i=[]
for i in soup.find_all('a', class_="gs_ibl gsc_mp_anchor"):
    h5i.append(i.text.split()) 
    
h5i


# In[150]:


h5m=[]
for i in soup.find_all('span', class_="gs_ibl gsc_mp_anchor"):
    h5m.append(i.text) 
    
h5m


# In[151]:


print(len(rank),len(publication),len(h5i),len(h5m))


# In[152]:


#Creating DataFrame

import pandas as pd

top_pub = pd.DataFrame({'Rank': rank,'Publication':publication, ' H5-index': h5i, ' H5-median': h5m})
top_pub

