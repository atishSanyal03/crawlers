# coding: utf-8
from Trial import *

players=[]
position=0
def playersPage():
    global players,position
    activate=False
    i=0
    x=0
    for text in urlText:
            #print text
            x += 1
            if x > position:
                position += 1
                if "View player information" in text or "next match" in text:
                    player={}
                    if "View player information" in text:
                        player['status']="Okay"
                    if "next match" in text:
                        if '%' in text:
                            if '25' in text:
                                player['status'] = "Highly Unlikely"
                            if '50' in text:
                                player['status'] = "Unlikely"
                            if '75' in text:
                                player['status'] = "Maybe"
                        else:
                            player['status'] = "No"
                if "FWD" in text or "MID" in text or "GKP" in text or "DEF" in text:
                    player['name']=cleanName(urlText[i-4])


                    player['team']=str(urlText[i-2])
                    player['pos']=str(text)
                    player['price']=str(urlText[i+5].encode('utf-8').replace('£',''))
                    player['form'] = str(urlText[i + 9])
                    player['points'] = str(urlText[i + 11])
                    player['bps'] = str(urlText[i + 13])
                    print player

            i+=1

def cleanName(name):
    if 'ä' in name.encode('utf-8'):
        name = name.encode('utf-8').replace('ä', 'a')
    if 'á' in name.encode('utf-8'):
        name = name.encode('utf-8').replace('á', 'a')
    if 'Ö' in name.encode('utf-8'):
        name = name.encode('utf-8').replace('Ö', 'O')
    if 'í' in name.encode('utf-8'):
        name = name.encode('utf-8').replace('í', 'i')
    if 'é' in name.encode('utf-8'):
        name = name.encode('utf-8').replace('é', 'e')
    if 'à' in name.encode('utf-8'):
        name = name.encode('utf-8').replace('à', 'a')
    if 'ü' in name.encode('utf-8'):
        name = name.encode('utf-8').replace('ü', 'u')
    if 'ó' in name.encode('utf-8'):
        name = name.encode('utf-8').replace('ó', 'o')
    if 'ø' in name.encode('utf-8'):
        name = name.encode('utf-8').replace('ø', 'o')
    if 'ß' in name.encode('utf-8'):
        name = name.encode('utf-8').replace('ß', 'ss')
    if 'ö' in name.encode('utf-8'):
        name = name.encode('utf-8').replace('ö', 'o')



    return str(name)

login()
scrapeURL("https://fantasy.premierleague.com/a/statistics/bps")
for i in range(0,16):
    if i!=0:
        browser.find_element_by_xpath('//a[@href="#' + str(i + 1) + '"]').click()
        time.sleep(5)
        lParser.feed(browser.page_source)
    else:
        scrapeURL("https://fantasy.premierleague.com/a/statistics/bps")
    playersPage()

#pointsPage()