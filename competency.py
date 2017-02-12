import sys
sys.path.append('/Users/HarshaGoli/Git/Rico')
github_score = __import__('getgithubscore')
so_score = __import__('stackovflodata')

def score(username='arshbot', name='Harsha Goli', location = 'Atlanta, GA, United States'):
	return github_score.final_score(username) + so_score.final_score(name, location)