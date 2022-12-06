from uuid import uuid4
class Auth:
    def __init__(self, root):
        self._root=root

        self._log=self._root._log
        self._db=self._root._db

        
    def login(self, user_email:str, password_hash:str, **kwargs):
        user=self._db.get_user_by_user_email(user_email=user_email)
        session=self._db.get_session_by_user_email(user_email=user['user_email'])
        
        
        if not user:
            return False
        
        if password_hash==user['password_hash']:
            self._log.success(
                'Password for {user_email} is correct'.format(
                    user_email=user['user_email']
                ))
            
            if not session:
                self._log.info(
                    """Existing session for user {user_email} weren't been found. starting login procedure""".format(
                        user_email=user['user_email']
                    ))
                    
                session_uuid=uuid4()
                session=self._db.create_session(
                    user_email=user_email,
                    session_uuid=session_uuid
                    )
                
                self._log.success(
                    'Session for {user_email} has been created successfully'.format(
                        user_email=user['user_email']
                ))
        
            return session
        
        else:
            return False
    
    def logout(self, user_email:str, session_uuid:str, **kwargs):
        self._log.info(
            'Trying to logout the {user_email}(session_uuid:{session_uuid})'.format(
                user_email=user_email,
                session_uuid=session_uuid
                )
            )
        
        status=self._db.remove_session(
            user_email=user_email,
            session_uuid=session_uuid
            )
        return status
        