from Message import Message
from Exceptions import RedirectionQueryExists
class create_short_url:
	def create_short_url(self, redirection_query: str, redirection_url: str, **kwargs):
		msg=Message()

		try:
			result=self._middlewares.url_shortener.create_short_url(
				redirection_query=redirection_query,
				redirection_url=redirection_url
				)
			msg.status="Success"
			msg.message="Short URL has been created."
			msg.data[result['redirection_uuid']]=result

		except RedirectionQueryExists:
			msg.status="Error"
			msg.message="Short URL hasn't been created. Redirection query do already exists."
		return msg