class Pixel_tracking:
    def __init__(self, root):
        self._root=root
        self._log=self._root._log
        
        self._db=self._root._db
    
    def get_pixel_tracker(self, tracker_uuid:str, **kwargs):
        tracker=self._db.get_pixel_tracker(
            tracker_uuid=tracker_uuid
            )
        del tracker['_id']

        return tracker

    def get_pixel_trackers(self, **kwargs):
        trackers=self._db.get_pixel_trackers()
        for tracker in trackers:
            del tracker['_id']

        return trackers
    
    def get_pixel_metrics(self, tracker_uuid:str, **kwargs):
        metrics=self._db.get_pixel_metrics(
            tracker_uuid=tracker_uuid
            )

        for metric in metrics:
            del metric['_id']
        
        return metrics