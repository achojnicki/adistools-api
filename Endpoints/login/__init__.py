from Message import Message
from Exceptions import UserDoNotExist, PasswordDoNotMatch

class login:
    def login(self, user_email:str, user_password:str, **kwargs):
        try:
            msg=Message()
            session=self._middlewares.auth.login(
                user_email=user_email,
                user_password=user_password
            )
        
            msg.status='Success'
            msg.message='Login Successful'
            msg.data['session_uuid']=session['session_uuid']
        
        except UserDoNotExist:
            msg.status='Failed'
            msg.message='User do not exist'
        
        except PasswordDoNotMatch:
            msg.status="Failed"
            msg.message="Wrong password"
        
        return msg