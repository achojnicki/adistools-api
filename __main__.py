from API import API
from adislog import adislog
from flask import Flask, request
from json import loads

api=API()
application=Flask(__name__)
application.config['TRAP_HTTP_EXCEPTIONS']=True

@application.route('/api/auth/login',methods=['POST'])
def login():
    return api.caller(api.login, request.form)

@application.route('/api/auth/logout',methods=['POST'])
def logout():
    return api.caller(api.logout, request.form) 

@application.route('/api/pixel_tracking/trackers',methods=["POST"])
def trackers():
    return api.caller(api.pixel_trackers, request.form)

@application.route('/api/pixel_tracking/tracker',methods=["POST"])
def tracker():
    return api.caller(api.pixel_tracker,request.form)

@application.route('/api/pixel_tracking/metrics', methods=["POST"])
def metrics():
    return api.caller(api.metrics, request.form)

@application.errorhandler(Exception)
def error_handler(error):
    return api.error(error)