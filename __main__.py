from API import API
from flask import Flask, request

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
def pixel_tracker_metrics():
    return api.caller(api.pixel_tracker_metrics, request.form)

@application.route('/api/url_shortener/urls', methods=["POST"])
def urls():
    return api.caller(api.shortened_urls, request.form)

@application.route('/api/url_shortener/url', methods=["POST"])
def url():
    return api.caller(api.shortened_url, request.form)

@application.route('/api/url_shortener/metrics', methods=["POST"])
def url_metrics():
    return api.caller(api.shortened_url_metrics, request.form)

@application.errorhandler(Exception)
def error_handler(error):
    return api.error(error)