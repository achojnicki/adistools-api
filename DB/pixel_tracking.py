class pixel_tracking:
    def get_pixel_tracker(self, tracker_uuid:str):
        query={"tracker_uuid":tracker_uuid}
        
        tracker={}
        cursor=self._pixel_trackers.find_one(query)
        
        for item in cursor:
            tracker[item]=cursor[item]

        return tracker
        
    def get_pixel_trackers(self):
        trackers=[]
        cursor=self._pixel_trackers.find()

        for item in cursor:
            trackers.append(item)

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
        query={"tracker_uuid": tracker_uuid}
        
        metrics=[]
        cursor=self._pixel_trackers_metrics.find(query)
        for item in cursor:
            metrics.append(item)

        return metrics
            