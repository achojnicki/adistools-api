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
        try:
            trackers=self._pixel_tracking.get_pixel_trackers()
            msg.status="Success"
            msg.message="Trackers"
            for a in trackers:
                msg.data[a['tracker_uuid']]=a
        except:
            msg.status="Error"
            msg.message="Unable to obtain tracker"

        return msg
    
    def pixel_tracker(self, tracker_uuid:str, **kwargs):
        msg=Message()
        try:
            tracker=self._pixel_tracking.get_pixel_tracker(
                tracker_uuid=tracker_uuid
                )
        
            msg.status='Success'
            msg.message='Tracker'
            msg.data[tracker['tracker_uuid']]=tracker
 
        except:
            msg.status="Error"
            msg.message="Unable to obtain tracker details"

        return msg

    def pixel_tracker_metrics(self, tracker_uuid:str, **kwargs):
        msg=Message()
        
        try:
            metrics=self._pixel_tracking.get_pixel_metrics(
                tracker_uuid=tracker_uuid
                )
            msg.status="Success"
            msg.message="Metrics"
            msg.data[tracker_uuid]=metrics
        except:
            msg.status="Error"
            msg.message="Unable to obtain metrics."
        
        return msg

    def shortened_urls(self, **kwargs):
        msg=Message()

        try:
            urls=self._url_shortener.get_urls()
            
            msg.status="Success"
            msg.message="Shortened urls"
            msg.data=urls
        except:
            msg.status="Error"
            msg.message="Unable to obtain URLs"
        return msg
    
    def shortened_url(self, url_uuid:str, **kwargs):
        msg=Message()

        try:
            url=self._url_shortener.get_url(
                url_uuid=url_uuid
                )
            msg.status="Success"
            msg.message="Shortened URL"
            msg.data[url_uuid]=url
        except:
            msg.status="Error"
            msg.message="Unable to obtain URL"
        return msg

    def shortened_url_metrics(self, url_uuid: str, **kwargs):
        msg=Message()

        try:
            metrics=self._url_shortener.get_url_metrics(
                url_uuid=url_uuid
                )
            msg.status="Success"
            msg.message="Metrics for shortened URL"
            msg.data[url_uuid]=metrics
        
        except:
            raise
            msg.status="Error"
            msg.message="Unable to obtain metrics for specific URL"
        return msg