import urllib
import HTMLParser
from selenium import webdriver
import time
urlText=[]

class parseText(HTMLParser.HTMLParser):
    def handle_data(self, data):
        data=data.strip(" ")
        if data != '\n':
            urlText.append(data)
lParser = parseText()
browser = webdriver.Chrome()
url="https://www.gmail.com"
browser.get(url)
time.sleep(5)
u = browser.find_element_by_xpath('//*[@id="identifierId"]')
u.send_keys("kumarjohn649@gmail.com")
#p = browser.find_element_by_id("ismjs-password")
#p.send_keys(password)
browser.find_element_by_xpath('//*[@id="identifierNext"]').click()
time.sleep(5)
pas=browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
pas.send_keys("autocar18-")
browser.find_element_by_xpath('//*[@id="passwordNext"]').click()
time.sleep(5)
a=browser.find_elements_by_tag_name("Welcome to Pocket!")
print a
#lParser.feed(urllib.urlopen("https://mail.google.com/mail/u/0/#inbox").read())
#lParser.close()
print urlText
print "Grab"
for text in urlText:
    print text