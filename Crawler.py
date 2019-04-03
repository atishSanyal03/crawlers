import urllib
from html.parser import HTMLParser
import urllib.request
import pandas as pd
urlText=[]
class parseText(HTMLParser):
    def handle_data(self, data):
        data=data.strip(" ").replace("\\n","").replace("\\r","").replace("\\t","")
        if data != '':
            urlText.append(data)

def scrapeAndPrint():
    lParser = parseText()

    url="https://tieba.baidu.com/f?kw=%E6%97%85%E8%A1%8C%E9%9D%92%E8%9B%99&ie=utf-8&pn=9600"
    with urllib.request.urlopen(url) as urlf:
        s = urlf.read()

    lParser.feed(s.decode('utf-8'))
    lParser.close()
    #print (urlText)
    totalString=""
    print (len(urlText))
    for text in urlText:
        totalString+=text
    return totalString


# articles=getArticles()
# uselessCount=0
# jsonArray=[]
# i=0
# for article in articles:
#     print (i)
#     # if i>10:
#     #     break
#     i+=1
#     try:
#         allWords=scrapeAndPrint(article)
#         urlText = []
#         jsonArray.append({'link':article,'allText': allWords })
#     except Exception as e:
#         print ("Cannot scrape")
#         jsonArray.append({'link': article, 'allText': []})
#         uselessCount+=1
# with open('ArticleDatabase.json', 'w') as f:
#     for item in jsonArray:
#         f.write("%s\n" % item)
# print (uselessCount)

print (scrapeAndPrint())
# print ('陈妞妞')