###
## FB == FireBase
##3

from firebase import firebase

firebase = firebase.FirebaseApplication('https://rico-8a81e.firebaseio.com/', None)

def upload_resume(tags):
	firebase.post("/resumes", tags)

def register_user(username):
	firebase.post("/users", username)

def usernames():
	return firebase.get("/users", None)