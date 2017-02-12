from nltk.corpus import stopwords
import PyPDF2
import fb
import devpost 
import rico

def score_resume(job_description, resume_path):
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
    
    name = " ".join(stripped_resume[0:2])


    usernames = fb.usernames()
    username = list(set(usernames) & set(stripped_resume))
    if len(username) > 0:
        tag = devpost.get_tags(username)
        tag_insct = list(set(stripped_resume) & set(tag))
        tag_score = len(tag_insct)  / len(stripped_resume)
        tag_score_adjusted = tag_score + (tag_score * .25)
        obj["devpost"] = {
            "score": tag_score_adjusted,
            "keywords": tag_insct
        }


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