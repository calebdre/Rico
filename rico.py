jobmatch = __import__('jobmatch')
competency = __import__('competency')
def score(tags={'listing_tags':[], 'candidate_tags':[]}, ghusername='arshbot', name, location):
	j = jobmatch.score(tags['listing_tags'], tags['candidate_tags'])
	c = competency.score(ghusername, name, location)
	return j+c
# tags = {'listing_tags':['Swift', 'Python', 'Java'], 'candidate_tags':['Swift', 'Python', 'perl', 'shot']}
# print(score(tags, 'youngvz'))
