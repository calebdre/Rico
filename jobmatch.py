def score(listing_tags=[], candidate_tags=[]):
	raw_score = set(listing_tags) & set(candidate_tags)
	raw_score = list(raw_score)
	print(listing_tags)
	print(candidate_tags)
	print(list(raw_score))
	return (len(raw_score) / float(len(listing_tags)))*100