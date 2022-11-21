from API import API
from adislog import adislog
from flask import Flask, request
from json import loads
import config

api=API()
app=Flask(__name__)

@app.route('/api/auth/login',methods=['POST'])
def login():
    return api.caller(api.login, request.form)


@app.route('/api/auth/logout',methods=['POST'])
def logout():
    return api.caller(api.logout, request.form) 


@app.route('/api/pixel_tracking/trackers',methods=["POST"])
def trackers():
    return api.caller(api.pixel_trackers, request.form)


@app.route('/api/pixel_tracking/tracker',methods=["POST"])
def tracker():
    return api.caller(api.pixel_tracker,request.form)

@app.route('/api/pixel_tracking/metrics', methods=["POST"])
def metrics():
    return api.caller(api.metrics, request.form)


@app.route('/api/')
def index():
    return 'working'

if __name__=='__main__':
    app.run()
else:
    application=app
