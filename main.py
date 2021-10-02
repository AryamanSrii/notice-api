from flask import Flask, jsonify, request
import utils

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" 
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response


@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "this is the" : "notice api"
    })


@app.route('/addNotice', methods=['GET'])
def addNotice():
    notice = request.args.get('notice')
    resp = utils.add_notice(notice)
    return jsonify({
        "response" : resp 
    })

@app.route('/getNotices', methods=['GET'])
def getNotices():
    resp = utils.get_notices()
    return jsonify({
        "response" : resp 
    })



if __name__ == '__main__':
    utils.create_table()
    app.run(debug=True)
