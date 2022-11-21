#submodules
from DB import DB
from Auth import Auth
from Message import Message
from Pixel_tracking import Pixel_tracking

from API.Endpoints import Endpoints

#external modules
from adislog import adislog
from flask import Response

import config
import inspect


class ArgsCheckException(Exception):
    pass

class MissingField(ArgsCheckException):
    pass

class WrongTypeForArg(ArgsCheckException):
    pass

class API(Endpoints):
    _config=config
    _db=None
    _log=None
    _auth=None
    _pixel_tracking=None

    def __init__(self):
        self._config=config

        self._log=adislog(
            backends=['terminal_table'],
            debug=True,
            replace_except_hook=False,
            )

        self._db=DB(self)
        self._auth=Auth(self)
        
        self._pixel_tracking=Pixel_tracking(self)
        
        self._endpoints_with_required_login=[
            self.logout,
            self.pixel_tracker,
            self.pixel_trackers,
            ]


    def caller(self, target, args):        
        #checking exist
        try:
            self._check_required_args(target, args)
        
        except MissingField as e:
            msg=Message()
            msg.type="Error"
            msg.message="Missing POST args for this request."
            msg.data['missing_fields']=e.missing_fields
            
            return msg.__str__()
        
                        
        if self._check_if_login_is_required(target):

            if not self._db.session_exists(args['session_uuid']):
                msg=Message()
                msg.type='Error'
                msg.message='This endpoint do require valid session.'
            
                return msg.__str__()
        
        
        return Response(
            target(**args).__str__().encode('utf-8', errors='replace'),
            mimetype="application/json"
            )
    
    def _check_if_login_is_required(self, endpoint):
        if endpoint in self._endpoints_with_required_login:
            return True
        return False
    
    def _check_args_types(self, caller, params):
        #TODO: finish it
        sig=inspect.signature(caller)
        
        wrong_types={}
        
        for param in sig.parameters:
            if sig.parameters[param].annotation!=inspect._empty:
                if type(params[param]) is not sig.parameters[param].annotation:
                    wrong_types[param]={'expected':param.annotation, 'got':type(params[param])}
        
        if len(wrong_types)>0:
            exception=WrongTypeForArg()
            exception.wrong_types=wrong_types
            
            raise exception
                
    def _check_required_args(self, caller, avaiable_params):        
        sig=inspect.signature(caller)
        required_params=[]
        
        for param in sig.parameters:
            if sig.parameters[param].default is inspect._empty:
                required_params.append(param)
                
        missing_params=required_params.copy()
        if 'kwargs' in missing_params:
            del missing_params[missing_params.index('kwargs')]
        
        for param in required_params:
            if param in avaiable_params:
                del missing_params[missing_params.index(param)]

        
        if len(missing_params)>0:
            exception=MissingField()
            exception.missing_fields=missing_params
            
            raise exception
        
    
