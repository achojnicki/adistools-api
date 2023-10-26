from DB import DB
from Response import Response
from Endpoints import Endpoints
from Exceptions import MissingField
from Middlewares import Middlewares

from adisconfig import adisconfig
from adistoolslog import adistoolslog
from flask import Response as Flask_Response

import inspect


class API:
    project_name="adistools-api"
    def __init__(self):
        self.config=adisconfig('/opt/adistools/configs/adistools-api.yaml')

        self.log=adistoolslog(
            project_name="adistools-api",
            backends=['rabbitmq_emitter'],
            rabbitmq_host=self.config.rabbitmq.host,
            rabbitmq_port=self.config.rabbitmq.port,
            rabbitmq_user=self.config.rabbitmq.user,
            rabbitmq_passwd=self.config.rabbitmq.password,
            debug=self.config.log.debug,
            )

        self.log.info('Starting initialization of adistools-api')
        
        self.db=DB(self)
        self.middlewares=Middlewares(self)
        self.endpoints=Endpoints(self)
            
        self.log.success('Initialisation of adistools-api successed.')

    def router(self, target, args):      
        """Router method - all valid traffic goes through this method"""
        #check if all required params are present. Otherwise raise exception.

        if not self.check_if_target_exists(target):
            rsp=Response()
            rsp.status="Error"
            rsp.message="Endpoint not found."

            return Flask_Response(rsp, mimetype="application/json", status=404)
        try:
            
            self._check_required_args(target, args)
        
        except MissingField as e:
            rsp=Response()
            rsp.status="Error"
            rsp.message="Missing POST args for this request."
            rsp.data['missing_fields']=e.missing_fields
            
            return Flask_Response(rsp, mimetype="application/json")

        #check if the endpoint require login. If so check if the session_uuid were provided and check existance of the session in the DB
        if self._check_if_login_is_required(target):
            if not self.db.session_exists(args['session_uuid']):
                rsp=Response()
                rsp.status='Error'
                rsp.message='This endpoint do require valid session.'
            
                return Flask_Response(rsp, mimetype="application/json")
        
        #call the endpoint
        return Flask_Response(
            getattr(self.endpoints,target)(**args),
            mimetype="application/json"
            )
    
    def check_if_target_exists(self, target):
        return hasattr(self.endpoints, target)

    def _check_if_login_is_required(self, target):
        if getattr(self.endpoints, target) in self.endpoints._endpoints_with_required_login:
            return True
        return False
                
    def _check_required_args(self, target, avaiable_params):
        sig=inspect.signature(getattr(self.endpoints,target))
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
        rsp=Response()

        rsp.status='Error'
        rsp.message=error.description
        
        return Flask_Response(rsp, mimetype="application/json", status=error.code)