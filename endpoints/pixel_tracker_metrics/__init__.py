from response import Response

class pixel_tracker_metrics:
    def pixel_tracker_metrics(self, pixel_tracker_uuid: str, **kwargs):
        rsp=Response()

        try:
            metrics=self._middlewares.pixel_tracker.get_pixel_tracker_metrics(
                pixel_tracker_uuid=pixel_tracker_uuid
                )
            rsp.status="Success"
            rsp.message="Metrics for pixel tracker"
            rsp.data[pixel_tracker_uuid]=metrics
        
        except:
            rsp.status="Error"
            rsp.message="Unable to obtain metrics for specific URL"
        return rsp