import sys
sys.path.append('/Users/HarshaGoli/Git/Rico')
github_score = __import__('getgithubscore')

def score(username='arshbot'):
	return github_score.final_score(username)