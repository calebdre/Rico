jobmatch = __import__('jobmatch')
competency = __import__('competency')
def score(tags={'listing_tags':[], 'candidate_tags':[]}, ghusername='arshbot'):
	j = jobmatch.score(tags['listing_tags'], tags['candidate_tags'])
	c = competency.score(ghusername)
	return j+c


tags = {'listing_tags':['Swift',
 						'Python',
 						'Java',
 						'Perl',
 						'Objective C',
 						'PHP',
 						'Cobalt'],
 		'candidate_tags':['Swift',
 						'Python',
 						'Java',
 						'Perl',
 						'Objective C',
 						'Javascript',
 						'Cobalt']}
print(score(tags, 'youngvz'))