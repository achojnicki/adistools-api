from response import Response

class pixel_trackers:
    def pixel_trackers(self, page=1, **kwargs):
        rsp=Response()

        pixel_trackers=self._middlewares.pixel_tracker.get_pixel_trackers(
            page=page
            )
        
        rsp.status="Success"
        rsp.message="Pixel trackers"
        rsp.data=pixel_trackers
        return rsp