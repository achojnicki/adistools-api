
class Pixel_tracking:
    def __init__(self, root):
        self._root=root
        self._log=self._root._log
        
        self._db=self._root._db
    
    def pixel_trackers(self, **kwargs):
        trackers=self._db.get_pixel_trackers()
        return trackers
    
    def pixel_tracker(self, tracker_uuid:str, **kwargs):
        tracker=self._db.get_pixel_tracker(
            tracker_uuid=tracker_uuid
            )
        return tracker
    
    def get_metrics(self, tracker_uuid:str, **kwargs):
        metrics=self._db.get_metrics(
            tracker_uuid=tracker_uuid
            )
        return metrics