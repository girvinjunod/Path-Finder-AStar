from flask import Flask, flash, request, redirect, url_for, session,jsonify
from flask.wrappers import Response
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import json



# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})


# sanity check route
@app.route('/', methods=['GET','POST','DELETE'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def getter1():
    data = request.get_json()
    print(data["edges"])
    print(data["nodes"])

    return "yes"

if __name__ == '__main__':
    app.run()