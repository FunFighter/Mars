#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from lxml import html
from bs4 import BeautifulSoup
from splinter import Browser
import requests as req
import shutil


# In[2]:
def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=True)


def mars_data_dict():


    browser = init_browser()
    # ### Nasa News Data

    # In[3]:


    url = "https://mars.nasa.gov/news/"
    browser.visit(url)


    # In[4]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[5]:


    # results = soup.find_all('ul',class_="item_list")


    title_res = soup.find('div', class_='content_title')
    title = title_res.text 

    body_res = soup.find('div', class_='article_teaser_body')
    body = body_res.text

    # date = soup.find("div", class_="list_date").text


    # ### Image Data

    # In[6]:


    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)

    image_html = browser.html
    i_soup = BeautifulSoup(image_html, 'html.parser')


    # In[7]:


    image = i_soup.find("img", class_="thumb")["src"]
    img_link = "https://jpl.nasa.gov"+image

    # ### Twitter Data

    # In[9]:


    twitter_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(twitter_url)

    twitter_html = browser.html
    t_soup = BeautifulSoup(twitter_html, 'html.parser')


    # In[10]:


    twitter_res = t_soup.find_all('div', class_='js-tweet-text-container')[0].text


    # In[11]:


    # This cleans text and removes the link from the image coming in.
    tweet = twitter_res.replace('\n','').split('pic.twitter')[0]


    # In[12]:


#     tweet


    # ### Mars Facts

    # In[13]:


    facts_url = 'https://space-facts.com/mars/'


    # In[14]:


    # we had the [0] at the end to remove the dataframe from the list
    facts_df = pd.read_html(facts_url)[0]
    facts_df.columns = ['Records:','Data']


    # In[15]:


    facts_df.set_index('Records:',inplace=True)


    # In[16]:


    facts_html = facts_df.to_html()


    # In[17]:




    # ### Mars Hemispheres

    # In[18]:


    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemi_url)

    hemi_html = browser.html
    h_soup = BeautifulSoup(hemi_html, 'html.parser')

    # base for attaching hrefs to make a full url
    base='https://astrogeology.usgs.gov'


    # In[19]:


    image_paths = h_soup.find_all('div',class_='item')


    # In[20]:


    paths = []
    for path in image_paths:
        p = path.a['href']
        paths.append(base + p)


    # In[21]:


    hemi_img_urls = []

    for path in paths:

        browser.visit(path)
        path_html = browser.html
        p_soup = BeautifulSoup(path_html, 'html.parser')

        title = p_soup.find('h2',class_='title').text

        for a in p_soup.find_all('a'):
            if a.text == 'Sample':
                hemi_dict = {'title' :title,'img_url':a['href']}
                hemi_img_urls.append(hemi_dict)



    # In[23]:


    browser.quit()


    # In[24]:


    mars_data_dict = {
            'title': title,
            'body': body,
            'image': img_link,
            'twitter' : tweet,
            'table' : facts_html,
            'hemisphere' : hemi_img_urls
        }


    # In[25]:


    return mars_data_dict


# In[ ]:




