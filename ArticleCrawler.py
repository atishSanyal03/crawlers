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

def scrapeAndPrint(url):
    lParser = parseText()

    #url="http://www.forbes.com/sites/kitconews/2014/03/12/gold-climbs-to-near-6-month-high-on-concerns-about-ukraine-china/"
    with urllib.request.urlopen(url) as urlf:
        s = urlf.read()

    lParser.feed(str(s))
    lParser.close()
    #print (urlText)
    totalString=""
    print (len(urlText))
    for text in urlText:
        totalString+=str(text.encode('utf-8'))
    return totalString

def getArticles():
    df=pd.read_csv("D:\\NUS Classes\Sem1\KDD\KaggleProject\\train.csv")
    return df['url'].tolist()
articles=getArticles()
uselessCount=0
jsonArray=[]
i=0
for article in articles:
    print (i)
    # if i>10:
    #     break
    i+=1
    try:
        allWords=scrapeAndPrint(article)
        urlText = []
        jsonArray.append({'link':article,'allText': allWords })
    except Exception as e:
        print ("Cannot scrape")
        jsonArray.append({'link': article, 'allText': []})
        uselessCount+=1
with open('ArticleDatabase.json', 'w') as f:
    for item in jsonArray:
        f.write("%s\n" % item)
print (uselessCount)


