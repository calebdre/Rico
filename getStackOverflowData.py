import requests
import simplejson as json


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
          user_id =    i['user_id']
          
          print ""
          print name
          print user_id
          print reputation

          getUserTimeline(user_id)


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
        if "post_type" in i and i['post_type'] == "question":
          
        print "Question "
        print i['title']
        print i['post_id']
        # if "detail" in i:
        #   print i['detail']
        print ""


    elif "post_type" in i and i['post_type'] == "answer":
        print "Answer" 
        print i['title']
        print i['post_id']
        # if "detail" in i:
        #   print i['detail']
        print ""



    

def main():
 getUserData("Caleb Lewis", "Atlanta, GA, United States")


main()
