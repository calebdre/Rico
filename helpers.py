from json import dumps
from datetime import datetime
from flask import Response

def respond_json(data):
    resp = Response(data, status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    print(resp.headers)
    return resp

def to_json(query):
    return respond_json(dumps((query)))

def error_message(message):
    return respond_json(dumps({"error": message}))

def success_message(message = "Success!"):
    return respond_json(dumps({"success":message}))
	
def respond_object(obj):
	return respond_json(dumps(obj))

def check_for_params(params, request):
    # TODO: check yet if we NEED the request object passed in or not
    missing_params = []
    for param in params:
        if param not in request.form:
            missing_params.append(param)

    if not missing_params:
        return None

    error_string = "Missing Parameters: "
    if missing_params:
        for param in missing_params:
            error_string += param + " "

    return error_string
