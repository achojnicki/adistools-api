from Message import Message

class login:
    def login(self, user_email:str, user_password:str, **kwargs):
        msg=Message()
        session=self._auth.login(
            user_email=user_email,
            user_password=user_password
        )
        
        if session:
            msg.status='Success'
            msg.message='Login Successful'
            msg.data['session_uuid']=session['session_uuid']
        
        else:
            msg.status='Failed'
            msg.message='Log in failed'
        
        return msg