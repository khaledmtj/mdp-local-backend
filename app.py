from flask import Flask, jsonify, request
import flask
from mdp_processing import ImageProcessing
import sys
import json

app = Flask(__name__)

@app.route('/')
def home():
	return jsonify("Hello rudy")

@app.route('/data',methods=['POST'])
def data_req():
        sys.stdout.write('data_req: 1-')
        req = flask.request.form["sample"]
        sys.stdout.write('data_req: 2\n')
##        resp = "Server received: " + req
##        json = {"textDetected": resp}
        imProc = ImageProcessing('processor')
        text = imProc.handleRotation(req)
        sys.stdout.write('data_req: 3\n')

        return text

@app.route('/errors',methods=['POST'])
def errors_req():
        sys.stdout.write('errors_req: 1-')
        req = flask.request.form["sample"]
        
        sys.stdout.write('errors_req: 2\n')
        imProc = ImageProcessing('processor')
        
        spell_errors = imProc.spell_corrector(req)
        sys.stdout.write('errors_req: 3\n')

        jsonData = {
                'spellErrors': spell_errors
                }
        jsonStr = json.dumps(jsonData, ensure_ascii=False)

        return jsonStr


# @app.route('/data/<string:name>')
# def get_data(name):
# 	return jsonify(name)




if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0")
