import re
import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd

todays_date = datetime.datetime.now()
date_stamp = str(todays_date.date())

# send a request to the webpage and get the html text
r = requests.get('https://www.tagesschau.de/')
soup = BeautifulSoup(r.text, 'html5lib')

links = []
texts = []
# search for all link tags on the page
a = soup.find_all('a')
# add the link and the corresponding teaser text to a list
# if it's from a paragraph of class 'dachzeile'
for item in a:
    if item.find('p', class_='dachzeile'):
        links.append(item.get('href'))
        texts.append(item.get_text())

# check which of the teaser texts are about corona / covid
# store them in a new list together with their link
corona_links = []
corona_texts = []
for i in range(len(texts)):
    if ('corona' in texts[i].lower()) | ('covid' in texts[i].lower()):
        if links[i].startswith('/'):
            corona_links.append(links[i])
            corona_texts.append(texts[i])

# get the full article from each of the corona_links
corona_articles = []
for link in corona_links:
    full_link = 'https://www.tagesschau.de' + link
    html = requests.get(full_link)
    sub_soup = BeautifulSoup(html.text, 'html5lib')
    # find all text paragraphs of class 'text small'
    article = sub_soup.find_all('p', class_='text small')
    paragraphs = []
    for i in range(len(article)):
        paragraphs.append(article[i].get_text())
    # join all paragraphs
    final_article = ' '.join(paragraphs)
    corona_articles.append(final_article)

# make DataFrame with one row per corona article
columns = ['date', 'url', 'article', 'resort']
df = pd.DataFrame(columns=columns)
df['url'] = corona_links
df['article'] = corona_articles
df['date'] = todays_date
df['resort'] = df['url'].apply(lambda x: x.split("/")[1])

# export DataFrame as csv file
df.to_csv('data/' + date_stamp)
