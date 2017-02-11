import requests

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

getusergitcommits()
