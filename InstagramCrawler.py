from selenium import webdriver
import time
from html.parser import HTMLParser
import re
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import traceback
urlText=[]
import json
class parseText(HTMLParser):
    def handle_data(self, data):
        data=data.strip(" ").strip("\n").strip(" ").strip()
        if data != '\n' or data!="":
            urlText.append(data)
browser = webdriver.Chrome()
lParser = parseText()

#function to get the post captions.
#Assumption here is that first 200 wil reflect overall nature of profile
def getCaptions(profileURL,pCount):
    browser.get(profileURL)
    time.sleep(1)
    allText={}
    limit=20 if int((pCount/10)+1)>20 else int((pCount/10)+1)
    for i in range(0,limit):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        elems=browser.find_elements_by_class_name("FFVAD")
        for e in elems:

            allText.setdefault(str(e.get_attribute("alt")),1)
    # print ("ALL IMAGE CAPTIONS ARE:")
    # for keys in allText:
    #     print (keys)
    return list(allText.keys())


#Login to instagram using a demo account created for the purpose of this project
def login(uname,pwd):
    browser.get("https://www.instagram.com/accounts/login/?source=desktop_nav")
    time.sleep(1)
    u=browser.find_element_by_name("username")
    u.send_keys(uname)
    p=browser.find_element_by_name("password")
    p.send_keys(pwd)
    browser.find_element_by_xpath("//*[contains(text(), 'Log in')]").click()

#function to get basic profile details
def getProfileDetails(profileURL):
    browser.get(profileURL)
    time.sleep(1)
    lParser.feed(browser.page_source)
    for text in urlText:
        if "This Account is Private" in text:
            return -1
    for text in urlText:
        if "window._sharedData" in text:
            t=text[21:len(text)-1]
            js=json.loads(t)
            name=str(js["entry_data"]["ProfilePage"][0]["graphql"]["user"]["full_name"])
            uName=js["entry_data"]["ProfilePage"][0]["graphql"]["user"]["username"]
            postCount=js["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]
            Id=js["entry_data"]["ProfilePage"][0]["graphql"]["user"]["id"]
            fCount=js["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_followed_by"]["count"]
            return  [name,uName,Id,fCount,postCount]

#function to list of followers
#Assumption the profile of first 1000 followers will reflect general pattern of followers
def getFollowerList(profileURL,fCount):
    browser.get(profileURL)
    time.sleep(1)
    browser.find_element(By.XPATH,"//*[@href='/"+str(profileURL.split('/')[-2])+"/followers/']").click()
    time.sleep(1)
    x = 600
    allFollowers={}
    limit= 20 if int((fCount/15)+1)>20 else int((fCount/15)+1)
    for i in range(0,limit):
        a=browser.find_elements_by_class_name("notranslate")
        for elem in a:
            if "FPmhX notranslate _0imsa" in elem.get_attribute("class"):
                allFollowers.setdefault(str(elem.get_attribute("href"),),1)
        eula = browser.find_element(By.XPATH, "//*[@class='isgrP']")
        browser.execute_script('arguments[0].scrollTo('+str(x-600)+', '+str(x)+')', eula)
        x+=600
        time.sleep(1)
    return list(allFollowers.keys())

login("cr7_singh_","BigData1234")
time.sleep(5)
profiles=['https://www.instagram.com/therealjuhisharma/']
num=0
allCollection=[]
while(num<len(profiles)):
    print (num)
    profileJson={}
    profileJson['link']=profiles[num]
    try:
        temp=getProfileDetails(profiles[num])

        urlText=[]
        if temp==-1:
            num+=1
            continue
        profileJson['name'],profileJson['uname'],profileJson['id'],profileJson['FCount'],profileJson['postCount']=temp
        if profileJson['FCount']>20000 or profileJson['postCount']<5:
            num+=1
            continue
        profileJson['captionArray']=getCaptions(profiles[num],profileJson['postCount'])
        profileJson['followers']=getFollowerList(profiles[num],profileJson['FCount'])

    except Exception as e:
        print ("Error")
        print (e)
        traceback.print_tb(e.__traceback__)
        num+=1
        continue
    profiles += profileJson['followers']
    allCollection.append(profileJson)
    num+=1
    if num>100: #Number of profiles you want to scroll
        break

with open('Dataset.json', 'w') as f:
     json.dump(allCollection,f)

browser.close()