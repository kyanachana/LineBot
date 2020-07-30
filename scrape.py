from bs4 import BeautifulSoup
import urllib.request
import json
import requests
import re
url = 'https://news.yahoo.co.jp/topics'
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) '\
    'AppleWebKit/537.36 (KHTML, like Gecko) '\
    'Chrome/84.0.4147.89 Safari/537.36'

def getNews(word):
    
    
    req = urllib.request.Request(url, headers={'User-Agent': ua})
    html = urllib.request.urlopen(req)
    soup = BeautifulSoup(html, "html.parser")
    #topics = soup.find('li > a') 
    #topicsindex = soup.find('div', attrs={'class': 'topicsindex'})
    topics = soup.select('li > a')

    count = 0
    list = []


    for topic in topics:
        #if topic.contents[0].find(word) != -1:
        if word in topic.contents[0]:
            list.append(topic.contents[0])
            list.append(topic.get('href'))
            count += 1

    if count == 0:
        list.append("記事が見つかりませんでした！！")

    result = '\n'.join(list)
    return result