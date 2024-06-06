import requests
import xml.etree.ElementTree as ET

RSS_FEED_URL = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"

def loadRSS():
    resp = requests.get(RSS_FEED_URL)
    
    return resp.content

def parseXML(rss):
    root = ET.fromstring(rss)
    
    newsitem = []
    
    for item in root.findall('./channel/item'):
        news = {}
        
        for child in item:
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')
        
        newsitem.append(news)
    
    return newsitem

def topStories():
    rss = loadRSS()
    
    newsitem = parseXML(rss)
    return newsitem