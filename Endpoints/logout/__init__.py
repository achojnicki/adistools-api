from Message import Message

class logout:
    def logout(self, user_email:str, session_uuid:str, **kwargs):
        msg=Message()
        status=self._middlewares.auth.logout(
            user_email=user_email,
            session_uuid=session_uuid
            )
        
        if status:
            msg.status="Success"
            msg.message='Logout successful'
        else:
            msg.status="Failed"
            msg.message='Logout failed'
        
        return msg