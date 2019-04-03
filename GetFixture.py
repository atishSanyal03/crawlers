from Trial import *
teams=["Arsenal","Leicester","Watford","Liverpool","Chelsea","Burnley","Crystal Palace","Huddersfield","Everton","Stoke","Southampton","Swansea","West Brom","Bournemouth","Brighton","Man City","Newcastle","Spurs","Man Utd","West Ham"]
position=0
def FixturesPage():
    global position
    activate=False
    pair=0
    last=""
    x=0
    for text in urlText:
        x+=1
        if x>position:
            position+=1
            #print text
            if "Sign Out" in text:
                activate=True
            if "Lead Partner" in text:
                activate=False
            if activate:
                for team in teams:
                    if team in text:
                        pair+=1
                        if pair==2:
                            print last, " Vs ", text
                            pair=0
                        last=text
                        #print text

login()
for i in range(0,3):
    gw=i+1
    print "\n\nFixtures for Gameweek\n ",str(gw)
    scrapeURL("https://fantasy.premierleague.com/a/fixtures/"+str(gw))
    FixturesPage()
    #urlText=[]
    #lParser=parseText()