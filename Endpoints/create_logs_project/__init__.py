from Response import Response
from Exceptions import LogsProjectExists

class create_logs_project:
	def create_logs_project(self, logs_project_name: str, **kwargs):
		rsp=Response()

		try:
			result=self._middlewares.logs.create_logs_project(
				logs_project_name=logs_project_name
				)
			rsp.status="Success"
			rsp.message="Log project has been created."
			rsp.data[result['logs_project_uuid']]=result
		
		except LogsProjectExists:
			rsp.status='Failed'
			rsp.message="Logs project with given name exists"
		
		return rsp