class pixel_tracker:
    def get_pixel_trackers(self, limit, skip):
        pixel_trackers=[]
        cursor=self.pixel_trackers.find().skip(skip).limit(limit)
        for item in cursor:
            pixel_trackers.append(item)
        return pixel_trackers

    def get_pixel_tracker(self, pixel_tracker_uuid: str):
        query={"pixel_tracker_uuid": pixel_tracker_uuid}

        pixel_tracker={}
        cursor=self.pixel_trackers.find_one(query)
        if cursor:
            for item in cursor:
                pixel_tracker[item]=cursor[item]

        return pixel_tracker

    def get_pixel_tracker_by_name(self, pixel_tracker_name: str):
        query={"pixel_tracker_name": pixel_tracker_name}

        pixel_tracker={}
        cursor=self.pixel_trackers.find_one(query)
        if cursor:
            for item in cursor:
                pixel_tracker[item]=cursor[item]

        return pixel_tracker
    

    def get_pixel_tracker_metrics(self, pixel_tracker_uuid: str):
        query={"pixel_tracker_uuid": pixel_tracker_uuid}
        
        metrics=[]
        cursor=self.pixel_trackers_metrics.find(query)

        for item in cursor:
            metrics.append(item)

        return metrics

    def create_pixel_tracker(self, pixel_tracker_uuid: str, pixel_tracker_name:str):
        document={
            'pixel_tracker_uuid' : str(pixel_tracker_uuid),
            'pixel_tracker_name' : pixel_tracker_name,
        }

        self.pixel_trackers.insert_one(document)
        return document

    def pixel_tracker_exists(self, pixel_tracker_name: str):
        return True if self.get_pixel_tracker_by_name(pixel_tracker_name=pixel_tracker_name) else False

    def delete_pixel_tracker(self, pixel_tracker_uuid: str):
        document={"pixel_tracker_uuid": pixel_tracker_uuid}

        self.pixel_trackers.delete_one(document)
