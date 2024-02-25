from response import Response
from exceptions import PixelTrackerDoesntExists

class delete_pixel_tracker:
	def delete_pixel_tracker(self, pixel_tracker_uuid: str, **kwargs):
		rsp=Response()

		try:
			result=self._middlewares.pixel_tracker.delete_pixel_tracker(
				pixel_tracker_uuid=pixel_tracker_uuid,
				)
			rsp.status="Success"
			rsp.message="Pixel tracker has been deleted."

		except PixelTrackerDoesntExists:
			rsp.status="Error"
			rsp.message="Pixel tracker hasn't been deleted as it doesn't exists."
		return rsp