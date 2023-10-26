from Response import Response

class logout:
    def logout(self, user_email:str, session_uuid:str, **kwargs):
        rsp=Response()
        status=self._middlewares.auth.logout(
            user_email=user_email,
            session_uuid=session_uuid
            )
        
        if status:
            rsp.status="Success"
            rsp.message='Logout successful'
        else:
            rsp.status="Failed"
            rsp.message='Logout failed'
        
        return rsp