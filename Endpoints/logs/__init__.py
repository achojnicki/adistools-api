from Message import Message

class logs:
    def logs(self, project_name=None, log_level=None, page=1, **kwargs):
        msg=Message()
        logs=self._logs.get_logs(
            page=page,
            project_name=project_name,
            log_level=log_level
        
            )
        
        msg.status="Success"
        msg.message="Logs"
        msg.data=logs
        return msg