import simplejson as json
import requests

questionsDictionary = {}
answersDictionary = {}

def final_score(name, location):
    rp = reputation_score(name, location)
    f_score = 0
    if rp > 25:
        f_score = 1
    elif rp > 50:
        f_score = 2
    elif rp > 80:
        f_score = 3
    elif rp > 200:
        f_score = 4
    elif rp > 300:
        f_score = 5
    elif rp > 400:
        f_score = 6
    elif rp > 600:
        f_score = 7
    elif rp > 800:
        f_score = 8
    elif rp > 1000:
        f_score = 9
    elif rp > 1500:
        f_score = 13
    elif rp > 2000:
        f_score = 15
    elif rp > 5000:
        f_score = 20

    return f_score

def reputation_score(name, location):
    rep_score = getUserData(name, location)
    print rep_score

def getUserData(name, location):
    baseUrl = "https://api.stackexchange.com/2.2/users?order=desc&sort=reputation&site=stackoverflow"
    baseUrl += formatName(name);
    r = requests.get(baseUrl)
    data = r.json()
    items = data['items']
    
    for i in items:
        if name == i['display_name']:
            if "location" in i and i['location'] == location:
                reputation = i['reputation']
                user_id = i['user_id']
                print ''
                print name
                print user_id
                return reputation
            #getUserTimeline(user_id)
    
def formatName(name):
    urlString = "&inname="
    array = name.split()
    urlString += array[0] + "_" + array[1]
    return urlString


def getUserTimeline(userId):
    userId = str(userId)
    baseUrl = "https://api.stackexchange.com/2.2/users/"
    
    urlString = baseUrl + userId + "/timeline?site=stackoverflow"
    
    r = requests.get(urlString)
    data = r.json()


    items = data['items']

    for i in items:
        print i
        if "post_type" in i and i['post_type'] == "question":
            postid = i['post_id']
            questionsDictionary[postid] = i['title']

        elif "post_type" in i and i['post_type'] == "answer":
            postid = i['post_id']
            answersDictionary[postid] = i['title']
    # printDictionary(questionsDictionary)
    # printDictionary(answersDictionary)


def printDictionary(dictionary):
    for question in dictionary:
        print dictionary[question]

# score("Harsha Goli", "Atlanta, GA, United States")
