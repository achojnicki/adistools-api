from response import Response
from exceptions import RedirectionQueryExists
class create_short_url:
	def create_short_url(self, redirection_query: str, redirection_url: str, **kwargs):
		rsp=Response()

		try:
			result=self._middlewares.url_shortener.create_short_url(
				redirection_query=redirection_query,
				redirection_url=redirection_url
				)
			rsp.status="Success"
			rsp.message="Short URL has been created."
			rsp.data[result['redirection_uuid']]=result

		except RedirectionQueryExists:
			rsp.status="Error"
			rsp.message="Short URL hasn't been created. Redirection query do already exists."
		return rsp