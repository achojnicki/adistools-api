from Message import Message
from Exceptions import LogsProjectExists

class create_logs_project:
	def create_logs_project(self, logs_project_name: str, **kwargs):
		msg=Message()

		try:
			result=self._middlewares.logs.create_logs_project(
				logs_project_name=logs_project_name
				)
			msg.status="Success"
			msg.message="Log project has been created."
			msg.data[result['logs_project_uuid']]=result
		
		except LogsProjectExists:
			msg.status='Failed'
			msg.message="Logs project with given name exists"
		
		return msg