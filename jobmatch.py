def score(listing_tags=[], candidate_tags=[]):
	raw_score = set(listing_tags) & set(candidate_tags)
	return (len(list(raw_score)) / float(len(listing_tags)))*100