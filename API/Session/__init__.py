class Session_Factory:
	def __init__(self, root):
		self._root=root
	
	def __call__(self, args, request):
		return Session(self._root, args, request)

class Session:
	def __init__(self, root, args, request):
		self._root=root

		self._request=request
		self._args=args





