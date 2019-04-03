# coding: utf-8
import urllib
import HTMLParser
import re
urlText=[]
class parseText(HTMLParser.HTMLParser):
    def handle_data(self, data):
        data=data.strip(" ")
        if data != '\n' or data!="":
            urlText.append(data)
lParser = parseText()

url="http://www.goal.com/en-sg/match/arsenal-vs-everton/2242129/live-commentary?ICID=MP_MS_3"
lParser.feed(urllib.urlopen(url).read())
lParser.close()
start=False
i=0
goals=[]
activateAssist=False
assists=[]
for text in urlText:
    if "FULL-TIME" in text or "Full time" in text or "Full Time" in text or "FULL TIME" in text or "Full-time" in text or "Full-Time" in text:
        start=True
    if start:
        if "Goal " in text:
            print text #,"    ", urlText[i+1]
            sr = re.findall("Goal[ ]*([A-Za-z éíáüöäÖ]*)", text.strip(" "),re.U)[0]
            goals.append(sr)
            activateAssist=True
        if "Assist" in text:
            print text
            sr = re.findall("Assist[ ]*([A-Za-z éíáüöäÖ]*)", text.strip(" "),re.U)[0]
            print sr
            if activateAssist:
                assists.append(sr)
                activateAssist=False
        if "Yellow Card" in text:
            print text
        if "Red Card" in text:
            print text
        if "Substitution" in text:
            print urlText[i-3],"  ", urlText[i+1],"    ",urlText[i+3]
        if "subs:" in text or "SUBS:" in text or "Subs:" in text :
            break
    i+=1
print "Goal Scorers: "
for goal in goals:
    print goal
print "Assists: "
for assist in assists:
    print assist