jobmatch = __import__('jobmatch')
github_score = __import__('getgithubscore')
so_score = __import__('stackovflodata')

def score(tags={'listing_tags':[], 'candidate_tags':[]}, ghusername='arshbot', name='Harsha Goli', location='Atlanta, GA, United States'):
	j = jobmatch.score(tags['listing_tags'], tags['candidate_tags'])
	g = github_score.final_score(ghusername)
	s = so_score.final_score(name, location)
	return j+g+s

#tags = {'listing_tags':['Swift', 'Python', 'Java'], 'candidate_tags':['Swift', 'Python', 'perl', 'shot']}
#print(score(tags, 'youngvz', 'Viraj Shaw', 'Atlanta, GA, United States'))
