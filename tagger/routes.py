from flask import request, jsonify
import json

@app.route('/'):
def index():
    response = {'response_code':200,
                'response_body':'This is the index page.'}
    return jsonify(response)
