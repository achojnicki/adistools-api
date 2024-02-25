from response import Response

class pixel_tracker:
    def pixel_tracker(self, pixel_tracker_uuid:str, **kwargs):
        rsp=Response()

        try:
            pixel_tracker=self._middlewares.pixel_tracker.get_pixel_tracker(
                pixel_tracker_uuid=pixel_tracker_uuid
                )
            rsp.status="Success"
            rsp.message="Pixel tracker"
            rsp.data[pixel_tracker_uuid]=pixel_tracker
        except:
            rsp.status="Error"
            rsp.message="Unable to obtain pixel tracker"
        return rsp