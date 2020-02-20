import requests
import flask
from flask import Flask, render_template, url_for, request, flash, redirect, jsonify, Response

# initialize our Flask application and the Keras model
app = flask.Flask(__name__)
app.debug = True
ROOT = str(app.root_path)

def get_demo_data():
    stat_url_root = 'https://osp-rs.stat.gov.lt/rest_json/'
    demo_query = 'data/S3R629_M3010217'
    res = requests.get(stat_url_root + demo_query).text

    return res

def get_demo_data2():
    stat_url_root = 'http://api.worldbank.org/v2/'
    demo_query = 'country/all/indicator/SP.POP.TOTL?date=2000:2001'
    r_format = '&format=json&per_page=1000'
    res = requests.get(stat_url_root + demo_query + r_format).text

    return res
    
def pass_call(query):
    stat_url_root = 'http://api.worldbank.org/v2/'
    r_format = '&format=json&per_page=1000'
    print(query)
    res = requests.get(stat_url_root + query + r_format).text

    return res

@app.route("/statistai_api1/<string:command>")
def statistai_api1(command):
    commands = {
        'demo': get_demo_data(),
        'demo2': get_demo_data2(),
        'pass': pass_call(request.args)
    }
    res = commands.get(command)
    resp = flask.make_response(res)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    
    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5500)
