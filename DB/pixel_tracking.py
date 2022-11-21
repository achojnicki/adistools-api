class pixel_tracking:
    def get_pixel_tracker(self, tracker_uuid:str):
        query={
            "tracker_uuid":tracker_uuid
            }
        
       
        result=self._pixel_trackers.find_one(query)
        del result['_id']
        return result
        
    def get_pixel_trackers(self):
        trackers=[]
        data=self._pixel_trackers.find()
        
        for tracker in data:
            del tracker['_id']
            trackers.append(tracker)
        
        return trackers
    
    def create_pixel_tracker(self, owner:str, tracker_uuid:str):
        document={
            "owner":owner,
            "tracker_uuid":tracker_uuid
            }
        
        try:
            self._pixel_trackers.insert_one(document)
            return True
        except:
            return False
    
    def get_metrics(self, tracker_uuid:str):
        query={
            "tracker_uuid": tracker_uuid
            }
        
        data=self._pixel_trackers_metrics.find(query)
        metrics=[]
        for metric in data:
            del metric['_id']
            metrics.append(metric)
        
        return metrics
            