from API import API
from flask import Flask, request

api=API()
application=Flask(__name__)
application.config['TRAP_HTTP_EXCEPTIONS']=True

@application.route('/auth/login',methods=['POST'])
def login():
    return api.caller(api.login, request.form)

@application.route('/auth/logout',methods=['POST'])
def logout():
    return api.caller(api.logout, request.form) 

@application.route('/url_shortener/urls', methods=["POST"])
def urls():
    return api.caller(api.shortened_urls, request.form)

@application.route('/url_shortener/url', methods=["POST"])
def url():
    return api.caller(api.shortened_url, request.form)

@application.route('/url_shortener/metrics', methods=["POST"])
def url_metrics():
    return api.caller(api.shortened_url_metrics, request.form)

@application.route('/url_shortener/create_short_url', methods=["POST"])
def create_short_url():
    return api.caller(api.create_short_url, request.form)

@application.route('/logs/logs', methods=["POST"])
def logs():
    return api.caller(api.logs, request.form)

@application.route('/logs/create_logs_project', methods=["POST"])
def create_log_project():
    return api.caller(api.create_logs_project, request.form)



@application.errorhandler(Exception)
def error_handler(error):
    return api.error(error)