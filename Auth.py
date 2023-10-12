from Exceptions import UserDoNotExist, PasswordDoNotMatch

from uuid import uuid4
from hashlib import sha256

class Auth:
    def __init__(self, root):
        self._root=root

        self._log=self._root._log
        self._db=self._root._db

        
    def login(self, user_email:str, user_password:str, **kwargs):
        user=self._db.get_user_by_user_email(user_email=user_email)
        if not user:
            raise UserDoNotExist
        
        session=self._db.get_session_by_user_email(user_email=user['user_email'])
        password_hash=sha256(user_password.encode('utf-8')).hexdigest()

        if password_hash==user['password_hash']:
            self._log.success(f'Password for {user["user_email"]} is correct')
            
            if not session:
                self._log.info(f'Existing session for user {user["user_email"]} weren\'t been found. Starting login...')
                    
                session_uuid=uuid4()
                session=self._db.create_session(
                    user_email=user['user_email'],
                    session_uuid=session_uuid,
                    user_uuid=user['user_uuid']
                    )
                
                self._log.success(f'Session for {user["user_email"]} has been created successfully')
        
            return session

        else:
            self._log.warning(f'password for user {user["user_email"]} is incorrect.')
            raise PasswordDoNotMatch
    
    def logout(self, user_email:str, session_uuid:str, **kwargs):
        self._log.info(f'Trying to logout the {user_email}(session_uuid:{session_uuid})')
        
        status=self._db.remove_session(
            user_email=user_email,
            session_uuid=session_uuid
            )
        return status
        