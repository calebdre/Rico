import requests
import simplejson as json


def getuserrepos(username='arshbot'):
	r = requests.get('https://api.github.com/users/'+username+'/repos')
	repos = r.json()
	list_of_repos = []
	if r.status_code == 404:
		print "Shit ain't found"
		return
	elif r.status_code == 200:
		for r in repos:
			list_of_repos.append(r['name'])
		print list_of_repos
		return list_of_repos

def getusergitcommits(username='arshbot'):
	repositories = getuserrepos(username)
	commitcount=0
	for r in repositories:
		rc = requests.get('https://api.github.com/repos/'+username+'/'+r+'/commits')
		repos=rc.json()
		commitcount+=len(repos)
	print commitcount

def main():
 getUserData("Stephen Muecke")
 getusergitcommits()



def getUserData(name):
    
    baseUrl = "https://api.stackexchange.com/2.2/users?order=desc&sort=reputation&site=stackoverflow"
    baseUrl += formatName(name);
    location = "Adelaide, Australia"


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
    
    print ""
    print "Questions"

    for i in items:
        
      post_type = i['post_type']
      
      if post_type == "question":
          
        print i['title']
        print i['detail']
        print ""


    print "Answers"

    for i in items:
    
    
      if post_type == "question":
                
        print i['title']
        print i['detail']
        print ""
    

main()
