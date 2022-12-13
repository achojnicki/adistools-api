from Message import Message

class Endpoints:
    def login(self, user_email:str, password_hash:str, **kwargs):
        msg=Message()
        session=self._auth.login(
            user_email=user_email,
            password_hash=password_hash
        )
        
        if session:
            msg.status='Success'
            msg.message='Login Successful'
            msg.data['session_uuid']=session['session_uuid']
        
        else:
            msg.status='Failed'
            msg.message='Log in failed'
        
        return msg


    def logout(self, user_email:str, session_uuid:str, **kwargs):
        msg=Message()
        status=self._auth.logout(
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
    
    
    
    def pixel_trackers(self, **kwargs):
        msg=Message()
        trackers=self._pixel_tracking.get_pixel_trackers()
        msg.status="Success"
        msg.message="Trackers"
        
        for a in trackers:
            msg.data[a['tracker_uuid']]=a
        
        return msg
    
    def pixel_tracker(self, tracker_uuid:str, **kwargs):
        msg=Message()
        tracker=self._pixel_tracking.get_pixel_tracker(
            tracker_uuid=tracker_uuid
            )
        
        if tracker:            
            msg.status='Success'
            msg.message='Tracker'
            msg.data[tracker['tracker_uuid']]=tracker
        else:
            msg.status="Error"
            msg.message="Tracker doesn't exists"

        return msg

    def metrics(self, tracker_uuid:str, **kwargs):
        msg=Message()
        
        try:
            metrics=self._pixel_tracking.get_metrics(
                tracker_uuid=tracker_uuid
                )
            msg.status="Success"
            msg.message="Metrics"
            msg.data[tracker_uuid]=metrics
        except:
            msg.status="Error"
            msg.message="Unable to obtain metrics."
        
        return msg
    