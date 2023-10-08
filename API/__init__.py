from DB import DB
from Auth import Auth
from Message import Message
from URL_shortener import URL_shortener
from API.Endpoints import Endpoints
from Exceptions import MissingField

from adisconfig import adisconfig
from adislog import adislog
from flask import Response

import inspect


class API(Endpoints):
    _config=None
    _db=None
    _log=None
    _auth=None
    _pixel_tracking=None

    def __init__(self):
        self._config=adisconfig('/opt/adistools/configs/adistools-api.yaml')

        self._log=adislog(
            backends=['terminal'],
            debug=True,
            replace_except_hook=False,
            )

        self._db=DB(self)

        self._auth=Auth(self)
        self._url_shortener=URL_shortener(self)
        
        self._endpoints_with_required_login=[
            self.logout,
            self.shortened_url,
            self.shortened_urls,
            self.shortened_url_metrics,
            self.create_short_url,

            ]


    def caller(self, target, args):      
        """Caller function - all valid traffic goes through this method"""
        #check if all required params are present. Otherwise raise exception.
        try:
            
            self._check_required_args(target, args)
        
        except MissingField as e:
            msg=Message()
            msg.status="Error"
            msg.message="Missing POST args for this request."
            msg.data['missing_fields']=e.missing_fields
            
            return Response(
                msg.__str__().encode('utf-8', errors='replace'),
                mimetype="application/json"
                )

        #check if the endpoint require login. If so check if the session_uuid were provided and check existance of the session in the DB
        if self._check_if_login_is_required(target):
            if not self._db.session_exists(args['session_uuid']):
                msg=Message()
                msg.status='Error'
                msg.message='This endpoint do require valid session.'
            
                return Response(
                   msg.__str__().encode('utf-8', errors='replace'),
                   mimetype="application/json"
                   )
        
        #call the endpoint
        return Response(
            target(**args).__str__().encode('utf-8', errors='replace'),
            mimetype="application/json"
            )
    
    def _check_if_login_is_required(self, target):
        if target in self._endpoints_with_required_login:
            return True
        return False
                
    def _check_required_args(self, target, avaiable_params):

        sig=inspect.signature(target)
        required_params=[]
        
        #iterate through the definitions of the endpoint to find out required arguments
        for param in sig.parameters:
            if sig.parameters[param].default is inspect._empty:
                required_params.append(param)
        
        #checking if the target is in the list of endpoints, which require valid session. if so adding the session_uuid param to the required list
        if self._check_if_login_is_required(target) and 'session_uuid' not in required_params:
            required_params.append('session_uuid')

        #checking if the kwargs is in the missing_poarams list. if so remove it.
        missing_params=required_params.copy()
        if 'kwargs' in missing_params:
            del missing_params[missing_params.index('kwargs')]
        
        #iterating trought the required params and checking if it is in avaiable params. if so then removing it form missing_params list.
        for param in required_params:
            if param in avaiable_params:
                del missing_params[missing_params.index(param)]

        #checking if the list of missing params is empty. if not raising exception.
        if len(missing_params)>0:
            exception=MissingField()
            exception.missing_fields=missing_params
            
            raise exception
    
    def error(self, error):
        """handler for error pages"""
        msg=Message()

        msg.status='Error'
        msg.message=error.description
        
        return Response(
            msg.__str__().encode('utf-8', errors='replace'),
            mimetype="application/json",
            status=error.code
        )