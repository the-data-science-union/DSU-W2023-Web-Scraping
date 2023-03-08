#!/usr/bin/env python
# coding: utf-8

# # BeautifulSoup Demo 

# ### Installing the Libraries

# In[1]:


pip install beautifulsoup4


# In[2]:


pip install requests


# In[3]:


pip install lxml


# ### Importing Libraries

# In[4]:


# import the libraries
from bs4 import BeautifulSoup
import requests


# ### Creating the Soup

# Using an example website with movie transcripts! 

# In[5]:


# define the link 
website = 'https://subslikescript.com/movie/Titanic-120338'


# In[6]:


# send request to website & save response 
result = requests.get(website)


# In[7]:


# obtain content 
content = result.text


# In[8]:


# 3. Create the soup
soup = BeautifulSoup(content, "lxml")


# In[9]:


# print HTML in readable format 
print(soup.prettify())


# Optional: Can go to website of the transcript and use "INSPECT" to find a smaller version of the HTML. 

# ### Locating Elements

# In[10]:


# use find() to get the first element that matches a specific tag name, class name, and id
# find_all() will get all the elements that matched and put them inside a list

# locate box that contains movie title, description, transcript 
box = soup.find('article', class_='main-article')

# note: opens with <article class = "main-article"> and ends with </article>
print(box)


# In[11]:


# locate movie title
# after locating title, get.text() obtains text inside the node 
# print to compare the difference 

title = box.find('h1').get_text()
print(box.find('h1'))
print(title)


# In[12]:


# locate transcript 
# inside a div tag w/ name "full-script"

transcript = box.find('div', class_='full-script')

# strip = True to remove leading/trailing spaces 
# spearator = ' ' so words have a blank space after every new line 
transcript = transcript.get_text(strip=True, separator=' ')

print(transcript)


# Now you know how to successfully scrape data from one page! 

# ### Exporting Data in a txt file

# In[13]:


# create txt file only saving the transcript variable 

with open(f'{title}.txt', 'w') as file:
    file.write(transcript)


# ### Scraping from Multiple Transcripts/Pages

# In[14]:


# root variable that will help us scrape multiple pages later.
root = 'https://subslikescript.com'
website = f'{root}/movies'


# In[15]:


# to locate multiple elements, add href=True to extract 
# corresponding link 
soup.find_all('a', href=True)


# In[16]:


# we have to loop through it and get the 
# hrefs one by one inside the loop.
for link in soup.find_all('a', href=True):
    link['href']


# In[17]:


# store the links using list comprehension 

links = [link['href'] for link in soup.find_all('a', href=True)]
print(links)


# In[18]:


# scrape the transcript of each link 

for link in links:
    result = requests.get(f'{root}/{link}')
    content = result.text
    soup = BeautifulSoup(content, 'lxml')


# # Source

# https://medium.com/geekculture/web-scraping-cheat-sheet-2021-python-for-web-scraping-cad1540ce21c#d859

# https://betterprogramming.pub/how-to-easily-scrape-multiple-pages-of-a-website-using-python-73e85bd06f8c
