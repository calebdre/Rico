from pyquery import PyQuery as pq
from helpers import *

def get_tags(username):
	d = pq(url='https://devpost.com/' + username)
	tags = d(".cp-tag.recognized-tag")
	keywords = [tag.text_content() for tag in tags]


	projects = d(".link-to-software")
	project_links = [link.attrib['href'] for link in projects]

	for link in project_links:
		p = pq(url=link)
		tags = p(".cp-tag.recognized-tag")
		project_tags = [tag.text_content() for tag in tags]
		keywords = keywords + project_tags

	return keywords
