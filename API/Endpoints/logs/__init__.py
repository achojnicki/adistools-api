from Message import Message

class logs:
    def logs(self,project_name=None, page=1, **kwargs):
        msg=Message()
        if not project_name:
            logs=self._logs.get_logs(
                page=page
                )
        else:
            logs=self._logs.get_logs_by_project_name(
                project_name=project_name,
                page=page
                )
        
        msg.status="Success"
        msg.message="Logs"
        msg.data=logs
        return msg