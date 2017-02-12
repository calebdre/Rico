from flask import Flask
from flask import request
from json import dumps
from helpers import *
from nltk.corpus import stopwords
import textract
import os
import re
import PyPDF2
import devpost

app = Flask(__name__)
stop_words = stopwords.words("english")
cwd = os.getcwd()

@app.route("/")
def index():
    pass

@app.route("/devpost")
def devpost_func():
    return to_json(devpost.get_tags("caleb_dre"))

@app.route("/parse", methods=["POST"])
def parse():
    job_description = request.form['job_description']
    path = cwd + "/file"
    request.files['file'].save(path)
    
    pdfFileObj = open(path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    resume = ""
    for page in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(page)
        resume += " " + pageObj.extractText()

    job_description = job_description.replace(",", "").replace("(", "").replace(")", "")
    resume = resume.replace(",", "").replace("(", "").replace(")", "").replace("\n", "")

    stripped_job_description = [word.lower().strip() for word in job_description.split() if word not in stop_words]
    stripped_resume = [word.lower().strip() for word in resume.split() if word not in stop_words]

    handle_regex = re.search("[\s|^]@\w+", resume)
    handle = handle_regex.group(1)

    matches = []

    for i, word in enumerate(stripped_job_description):
        for word2 in stripped_resume:
            if word2 in word:
                matches.append(word)

    matches = list(set(matches))
    return to_json(matches)

if __name__ == "__main__":
    app.run(debug=True)
