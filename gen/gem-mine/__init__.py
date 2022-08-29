# Copyright 2022, William L. Nortman, All Rights Reserved
import random

def addGemMineStory(world,burg,burgMarker):
    print(burgMarker)
    seed = burg['name'] + str(int(burgMarker['marker']['x'])) + str(int(burgMarker['marker']['y']))
    random.seed(seed) #Make sure it generates the same everytime
    numberOfNobles = getIndustryCount(burg,'Nobles')
    numberOfNoblesWithInterest = int(random.random() *numberOfNobles)
    for nobleCount in range(0,numberOfNoblesWithInterest):
        story = {}
        nobleInterested =  int(random.random() *numberOfNobles)
        #noble = getNoble(burg,nobleInterested)
        story['description'] = "The Noble"+ str(nobleInterested)  +" want this"
        burgMarker['stories'].append(story)


def getIndustryCount(burg, industrySearch):
    for industry in burg['domain']['demographics']['industries']:
        if industry['industry'] == industrySearch:
            return int(industry['count'])


