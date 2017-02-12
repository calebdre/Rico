from flask import Flask
from flask import request
from json import dumps
from helpers import *
import textract
import os
import re
import devpost
import score 

app = Flask(__name__)
cwd = os.getcwd()

@app.route("/")
def index():
    pass

@app.route("/devpost")
def devpost_func():
    return to_json(devpost.get_tags("caleb_dre"))
    

@app.route("/parse", methods=["POST"])
def parse():
    scores = {}

    job_description = request.form['job_description']
    path = cwd + "/file"
    request.files['file'].save(path)

    resume_score, matches = score.score_resume(job_description, path)

    scores["resume"] = {
        "score": resume_score,
        "keywords": ",".join(matches)
    }
    
    return to_json(scores)

if __name__ == "__main__":
    app.run(debug=True)
