from .auth import Auth
from .url_shortener import URL_shortener
from .logs import Logs

class Middlewares:
	def __init__(self, root):
		self._root=root

		self.auth=Auth(root)
		self.url_shortener=URL_shortener(root)
		self.logs=Logs(root)