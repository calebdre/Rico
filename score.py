from nltk.corpus import stopwords
import ResumeChecker
import PyPDF2
import fb
import devpost 
import rico
import os
import re

cwd = os.getcwd()

def score_resume(job_description, resume_path):
    df = ResumeChecker.create_resume_df(cwd)
    obj = {}
    stop_words = stopwords.words("english")
    pdfFileObj = open(resume_path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    resume = ""
    for page in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(page)
        resume += " " + pageObj.extractText()

    job_description = job_description.replace(",", "").replace("(", "").replace(")", "")
    resume = resume.replace(",", "").replace("(", "").replace(")", "").replace("\n", "")

    stripped_job_description = [word.lower().strip() for word in job_description.split() if word not in stop_words]
    stripped_resume = [word.lower().strip() for word in resume.split() if word not in stop_words]
    
    usernames = fb.usernames().values()
    username = None
    for u in usernames:
        found = re.findall(u, " ".join(stripped_resume))
        if len(found) > 0:
            username = found[0]
            break

    if username is not None: 
        tag = devpost.get_tags(username)
        if tag is not None:
            tag_insct = list(set(stripped_resume) & set(tag))
            tag_score = len(tag_insct)  / len(stripped_resume)
            tag_score_adjusted = tag_score + (tag_score * .25)
            obj["devpost"] = {
                "score": tag_score_adjusted,
                "keywords": tag_insct
            }

        name = " ".join(stripped_resume[0:2])
        location = re.findall("[A-Z]\w+\s[A-Z]\w+", job_description)[0]
        obj["name"] = name
        obj["location"] = location

        tags={'listing_tags':stripped_job_description, 'candidate_tags':stripped_resume}
        score = rico.score(tags, username, name, location) 
        obj["job_match_score"] = score[0]
        obj["github_score"] = score[1]
        obj["s_o_score"] = score[2]
        # obj

    matches = [word for word in stripped_job_description if word in stripped_resume]
    matches = list(set(matches))
    matches_count = len(matches)
	
	# this comes from the fact that not all terms in matches are relevent,
	# so we do this to attempt to correct. This is probably extremely wrong.
    matches_count_adjusted = matches_count + (matches_count * .25) 
    if matches_count_adjusted > 0:
        resume_score = matches_count_adjusted / len(stripped_job_description)
    else:
        resume_score = 0;

    obj["resume"] = {
        "score": resume_score,
        "keywords": ",".join(matches)
    }

    return  obj