import urllib
import HTMLParser

urlText=[]
class parseText(HTMLParser.HTMLParser):
    def handle_data(self, data):
        data=data.strip(" ")
        if data != '\n':
            urlText.append(data)
lParser = parseText()

url="https://www.cheapcheaplah.com/pages/grab-uber-taxi-promos"

lParser.feed(urllib.urlopen(url).read())
lParser.close()
print (urlText)
print ("Grab")
for text in urlText:
    if text!="":
        if "Share" in text or "Premium" in text:
          print (last,"\t",text)
        last=text
    if "Uber SG Coupons" in text:
        break
print ("\n\nUber")
for text in urlText:
    if text != "":
        if "POOL" in text:
          print (last,"\t",text)
        last=text
    if "ComfortDelGro Taxi (Comfort and CityCab) Coupons" in text:
        break