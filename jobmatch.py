def score(listing_tags=[], candidate_tags[]):
	raw_score = set(listing_tags) & set(candidate_tags)
	return (list(raw_score)[0]/float(len(listing_tags)))*100