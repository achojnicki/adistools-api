from Arg_parser.types.base_type import base_type

class str_type(base_type):
	def validate(self):
		try:
			str(self.value)