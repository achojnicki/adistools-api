from exceptions import PixelTrackerExists, PixelTrackerDoesntExists

from uuid import uuid4

class Pixel_tracker:
    def __init__(self, root):
        self._root=root

        self.config=self._root.config
        self.log=self._root.log
        self.db=self._root.db

    def get_pixel_trackers(self, page):
        limit=self.config.api.results_per_page
        skip=(int(page)-1)*limit

        pixel_trackers={}
        data=self.db.get_pixel_trackers(
            limit=limit,
            skip=skip
            )
        for item in data:
            del item['_id']

        for pixel_tracker in data:
            pixel_trackers[pixel_tracker['pixel_tracker_uuid']]=pixel_tracker

        self.log.success('Obtained details about a pixel trackers')

        return pixel_trackers

    def get_pixel_tracker(self, pixel_tracker_uuid: str):
        pixel_tracker=self.db.get_pixel_tracker(
            pixel_tracker_uuid=pixel_tracker_uuid
            )
        del pixel_tracker['_id']
        self.log.success('Obtained details about a pixel tracker')
        return pixel_tracker

    def get_pixel_tracker_metrics(self, pixel_tracker_uuid: str):
        metrics=self.db.get_pixel_tracker_metrics(
            pixel_tracker_uuid=pixel_tracker_uuid
            )
        for item in metrics:
            del item['_id']
        self.log.success('Obtained metrics of a pixel tracker')
        return metrics

    def create_pixel_tracker(self, pixel_tracker_name: str):
        if self.db.pixel_tracker_exists(pixel_tracker_name):
            raise PixelTrackerExists

        pixel_tracker_uuid=uuid4()

        document=self.db.create_pixel_tracker(
            pixel_tracker_uuid=pixel_tracker_uuid,
            pixel_tracker_name=pixel_tracker_name,
            )
        del document['_id']

        self.log.success(f'Pixel tracker {pixel_tracker_name}({pixel_tracker_uuid}) created.')
        return document

    def delete_pixel_tracker(self, pixel_tracker_uuid: str):
        if not self.db.get_pixel_tracker(pixel_tracker_uuid):
            raise PixelTrackerDoesntExists

        self.db.delete_pixel_tracker(pixel_tracker_uuid)


