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
def getter():
    data = request.get_json()
    print(data["edges"])
    print(data["nodes"])
    return "yes"

if __name__ == '__main__':
    app.run()

def matrixadj(listedge, listnode):
    matrixadj = [[0 for i in range(len(listnode))] for j in range(len(listnode))]
    for i in listedge:
        awal, akhir = i
        idxawal = listnode.index(awal)
        idxakhir = listnode.index(akhir)
        matrixadj[idxawal][idxakhir] = 1
        matrixadj[idxakhir][idxawal] = 1
    return matrixadj