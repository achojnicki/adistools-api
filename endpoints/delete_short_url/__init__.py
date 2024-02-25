from response import Response
from exceptions import RedirectionQueryDoesntExists

class delete_short_url:
	def delete_short_url(self, redirection_uuid: str, **kwargs):
		rsp=Response()

		try:
			result=self._middlewares.url_shortener.delete_short_url(
				redirection_uuid=redirection_uuid,
				)
			rsp.status="Success"
			rsp.message="Short URL has been deleted."

		except RedirectionQueryDoesntExists:
			rsp.status="Error"
			rsp.message="Short URL hasn't been deleted as it doesn't exists."
		return rsp