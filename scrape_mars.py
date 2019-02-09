#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Mission to Mars


# In[7]:


## Step 1 - Scraping
## NASA Mars News


# In[8]:


from bs4 import BeautifulSoup as bs
from splinter import Browser
from selenium import webdriver
import pandas as pd
import time 
import requests


# In[9]:


#url
nasa_url = "https://mars.nasa.gov/news/"
browser = Browser("chrome", headless = False)
browser.visit(nasa_url)
time.sleep(3)


# In[10]:


# HTML object
nasa_html = browser.html
# Parse HTML with BeautifulSoup
nasa_soup = bs(nasa_html, "html.parser")


# In[11]:


# Collect News Title
news_title = nasa_soup.find("div", class_ = "content_title").text.strip()
news_title


# In[12]:


### JPL Mars Space Images - Featured Image


# In[17]:


#url & parsing
jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser = Browser("chrome", headless = False)
browser.visit(jpl_url)
time.sleep(3)
browser.click_link_by_partial_text("FULL IMAGE")
time.sleep(3)
browser.click_link_by_partial_text("more info")


# In[18]:


#HTML
featured_image_html = browser.html
# Parse HTML with BeautifulSoup
jpl_soup = bs(featured_image_html, "html.parser")


# In[19]:


#get image url
featured_img = jpl_soup.find("figure", class_ = "lede")
featured_img_url =featured_img.a["href"]
featured_img_url = ("https://www.jpl.nasa.gov" + featured_img_url)
featured_img_url


# In[ ]:


### Mars Weather


# In[22]:


# URL & HTML
weather_url = "https://twitter.com/marswxreport?lang=en"
weather_html = requests.get(weather_url)
weather_soup = bs(weather_html.text, "html.parser")
time.sleep(3)


# In[23]:


mars_weather = weather_soup.find("p", class_ = "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text.strip()
mars_weather


# In[ ]:


### Mars Facts


# In[31]:


facts_url = "http://space-facts.com/mars/"
table = pd.read_html(facts_url)
table


# In[34]:


mars_facts = table[0]
mars_facts.columns = ["", ""]
mars_facts


# In[35]:


facts_table = mars_facts.to_html()
mars_facts_table = facts_table.replace("\n", "")
mars_facts_table


# In[ ]:


### Mars Hemispheres


# In[37]:


#create list
hemisphere_img_urls = []
hemisphere_dicts = {"title": [] , "img_url": []}


# In[38]:


# url
usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser = Browser("chrome", headless = False)
browser.visit(usgs_url)
time.sleep(3)
home_page = browser.html


# In[40]:


#HTML & Parsing
hemispheres_soup = bs(home_page, "html.parser")
results = hemispheres_soup.find_all("h3")
# Use loop 
for result in results:
    title = result.text
    print(title)
    title = title[:-9]
    print(title)
    browser.click_link_by_partial_text(title)
    time.sleep(1)
    img_url = browser.find_link_by_partial_href("download")["href"]
    print(img_url)
    hemisphere_dicts = {"title": title, "img_url": img_url}
    hemisphere_img_urls.append(hemisphere_dicts)
    time.sleep(1)
    browser.visit(usgs_url)

