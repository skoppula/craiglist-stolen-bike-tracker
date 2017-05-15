
# coding: utf-8

# In[92]:

from bs4 import BeautifulSoup
import urllib
import time
import random


# In[93]:

matches_path = "/home/skoppula/matches.txt"
required_keywords = [['bike','bicycle','cruiser']] # atleast one of each pair of words needs to occur to trigger
optional_keywords = ['vintage',['2008','2009']]
num_opt_keywords_required = 1
finds = []


# In[94]:

tld = "https://boston.craigslist.org"
r = urllib.urlopen(tld + '/search/bia').read()
soup = BeautifulSoup(r)
search_result_links = soup.find_all("a", class_="result-title hdrlnk")


# In[96]:

def check_words_against_filter(all_words):
    for required_kw_set in required_keywords:
        if isinstance(required_kw_set, basestring):
            if required_kw_set not in all_words: return  False
        else:
            pair_check = any([kw in all_words for kw in required_kw_set])
            if not pair_check: return False
            
    count = 0
    for optional_kw_set in optional_keywords:
        if isinstance(optional_kw_set, basestring):
            if optional_kw_set in all_words:
                count += 1
        else:
            pair_check = any([kw in all_words for kw in optional_kw_set])
            if pair_check: count += 1

    return count >= num_opt_keywords_required

def open_and_check_url(url):
    r = urllib.urlopen(url).read()
    soup = BeautifulSoup(r)
    title_dom_element = soup.find(id="titletextonly")
    description_dom_element = soup.find(id="postingbody")
    all_words = ""
    try:
        title = str(title_dom_element.get_text()).lower()
        description = str(description_dom_element.get_text()).lower().replace("qr code link to this post", "")
        all_words += title + description
    except:
        with open("matches.txt", "a") as myfile:
            myfile.write("Could not open " + url + ' or had zero/no title matches \n')
    # return all_words
    return check_words_against_filter(all_words)


# In[88]:

# testing
# all_words = open_and_check_url('https://boston.craigslist.org/nos/bik/6132576092.html')
# check_words_against_filter(all_words)


# In[97]:

for result_link in search_result_links:
    time.sleep(2 + random.random()) # circumvent anti-bot detection/spam rate limiting
    url = tld + result_link["href"]
    print url
    if(open_and_check_url(url)):
        finds.append(str(url))


# In[98]:

# print finds


# In[99]:

with open(matches_path, "a") as myfile:
    for url in finds:
        myfile.write(url + '\n')

