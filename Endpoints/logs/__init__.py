from response import Response

class logs:
    def logs(self, project_name=None, log_level=None, page=1, **kwargs):
        rsp=Response()
        logs=self._middlewares.logs.get_logs(
            page=page,
            project_name=project_name,
            log_level=log_level
        
            )
        
        rsp.status="Success"
        rsp.message="Logs"
        rsp.data=logs
        return rsp