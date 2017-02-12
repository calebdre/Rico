from datetime import timedelta
from flask import make_response, request, current_app
from flask_cors import CORS, cross_origin
from functools import update_wrapper
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
import ResumeChecker

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

cwd = os.getcwd()

@app.route("/")
def index():
    pass

@app.route("/devpost")
@cross_origin()
def devpost_func():
    return to_json(devpost.get_tags("caleb_dre"))
    

@app.route("/register-github", methods=["POST"])
@cross_origin()
def register_github():
    username = request.form['username']
    location = request.form['location']
    fb.register_user(username, location)
    return success_message("registered yay")

@app.route("/upload_resume")
def upload_resume():
    username = request.form['username']
    location = request.form['location']
    path = cwd + "/file.pdf"
    f = request.files['file']
    f.save(path)

    df = ResumeChecker.create_resume_df(cwd)

    fb.register_user(username, location)

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

@app.route("/red", methods=["POST"])
def red():
    job_description = request.form['job_description']
    path = cwd + "/file.pdf"
    f = request.files['file']
    f.save(path)

    
    json = ResumeChecker.create_resume_df(cwd).to_json()
    return Response(json, status=200, mimetype='application/json')
if __name__ == "__main__":
    app.run(debug=True)
