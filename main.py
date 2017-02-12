from flask import Flask
from flask import request
from helpers import *
import os
import re
import devpost
import score 
import rico
import fb
import zipfile

app = Flask(__name__)
cwd = os.getcwd()

@app.route("/")
def index():
    pass

@app.route("/devpost")
def devpost_func():
    return to_json(devpost.get_tags("caleb_dre"))
    

@app.route("/register-github", methods=["POST"])
def register_github():
    username = request.form['username']
    fb.register_user(username)
    return success_message("registered yay")

@app.route("/score", methods=["POST"])
def score_route():
    job_description = request.form['job_description']
    path = cwd + "/file"
    f = request.files['file']
    f.save(path)

    if f.filename.rsplit('.', 1)[1].lower() == "zip":
        newpath = cwd + "/zip"
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        zip_ref = zipfile.ZipFile(path, 'r')
        zip_ref.extractall(newpath)
        zip_ref.close()

        scores = []
        for f in os.listdir(newpath):
            fname = cwd + "/zip/" + f
            if len(fname.split(".")) > 1:
                scores.append(score.score_resume(job_description, fname))
    else:
        scores = score.score_resume(job_description, path)

    return to_json(scores)

if __name__ == "__main__":
    app.run(debug=True)
