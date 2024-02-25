from response import Response
from exceptions import PixelTrackerExists
class create_pixel_tracker:
	def create_pixel_tracker(self, pixel_tracker_name: str, **kwargs):
		rsp=Response()

		try:
			result=self._middlewares.pixel_tracker.create_pixel_tracker(
				pixel_tracker_name=pixel_tracker_name,
				)
			rsp.status="Success"
			rsp.message="Pixel tracker has been created."
			rsp.data[result['pixel_tracker_uuid']]=result

		except PixelTrackerExists:
			rsp.status="Error"
			rsp.message="Pixel tracker hasn't been created. Pixel tracker with given name do already exists."
		return rsp