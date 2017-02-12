from nltk.corpus import stopwords
import PyPDF2

def score_resume(job_description, resume_path):
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

    matches = [word for word in stripped_job_description if word in stripped_resume]
    matches = list(set(matches))
    matches_count = len(matches)
	
	# this comes from the fact that not all terms in matches are relevent,
	# so we do this to attempt to correct. This is probably extremely wrong.
    matches_count_adjusted = matches_count + (matches_count * .25) 
    resume_score = matches_count_adjusted / len(stripped_job_description)

    return  resume_score, matches