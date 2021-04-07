from flask import Flask, flash, request, redirect, url_for, session,jsonify
from flask.wrappers import Response
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import json
from abintang import *



# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})


# sanity check route
def matrixadj(listedge, listnode):
    matrixadj = [[0 for i in range(len(listnode))] for j in range(len(listnode))]
    for i in listedge:
        awal, akhir = i
        idxawal = listnode.index(awal)
        idxakhir = listnode.index(akhir)
        matrixadj[idxawal][idxakhir] = 1
        matrixadj[idxakhir][idxawal] = 1
    return matrixadj

@app.route('/', methods=['GET','POST','DELETE'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def getter():
    data = request.get_json()
    # print(data["edges"])
    # print(data["nodes"])
    bismillah = matrixadj(data["edges"], data["nodes"])
    matrixdistance = buatmatrixdistance(bismillah, data["nodes"])
    astar = astar2(data["selected"][0], data["selected"][1], bismillah, matrixdistance, data["nodes"])
    print(astar[1])
    return json.dumps([astar[1],astar[2],astar[3]])


if __name__ == '__main__':
    app.run()

