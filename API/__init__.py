from Exceptions import ValidationError

from API.Session import Session
from API.Form_Validator import Form_Validator
from DB import DB
from Response import Response
from Endpoints import Endpoints
from Middlewares import Middlewares

from adisconfig import adisconfig
from log import Log

from flask import Response as Flask_Response

import inspect

class API:
    project_name="adistools-api"
    def __init__(self):
        self.config=adisconfig('/opt/adistools/configs/adistools-api.yaml')

        self.log=adistoolslog(
            root=self,
            rabbitmq_host=self.config.rabbitmq.host,
            rabbitmq_port=self.config.rabbitmq.port,
            rabbitmq_user=self.config.rabbitmq.user,
            rabbitmq_passwd=self.config.rabbitmq.password,
            debug=self.config.log.debug,
            )

        self.log.info('Starting initialization of adistools-api')
        
        self.db=DB(self)
        self.middlewares=Middlewares(self)
        self.session=Session(self)
        self.endpoints=Endpoints(self)
        self.form_validator=Form_Validator(self)
            
        self.log.success('Initialisation of adistools-api successed.')

    def router(self, target, args, request):      
        """Router method - all valid traffic goes through this method"""

        #changing type to mutable one
        args=dict(args)

        if not self.check_if_target_exists(target):
            rsp=Response()
            rsp.status="Error"
            rsp.message="Endpoint not found."
            return Flask_Response(rsp, mimetype="application/json", status=404)
                 

        try:
            self.form_validator.validate(target, args)

        except ValidationError as e:
            rsp=Response()
            rsp.status="Error"
            rsp.message="Validation Error"
            rsp.data=e.error
            return Flask_Response(rsp, mimetype="application/json")


        #check if the endpoint require login. If so check if the session_uuid were provided and check existance of the session in the DB
        if self._check_if_login_is_required(target):
            if not self.db.session_exists(args['session_uuid']):
                rsp=Response()
                rsp.status='Error'
                rsp.message='This endpoint do require valid session.'
            
                return Flask_Response(rsp, mimetype="application/json")
        
        self.session.request=request
        #call the endpoint
        response=Flask_Response(
            getattr(self.endpoints,target)(**args),
            mimetype="application/json"
            )
        return response
    
    def check_if_target_exists(self, target):
        return hasattr(self.endpoints, target)

    def _check_if_login_is_required(self, target):
        if getattr(self.endpoints, target) in self.endpoints._endpoints_with_required_login:
            return True
        return False

    
    def error(self, error):
        """handler for error pages"""


        rsp=Response()
        rsp.status='Error'
        rsp.message=error.description 
        
        return Flask_Response(rsp, mimetype="application/json", status=error.code)