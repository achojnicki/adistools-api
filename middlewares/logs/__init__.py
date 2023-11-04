from exceptions import LogsProjectExists
from uuid import uuid4

class Logs:
    def __init__(self, root):
        self._root=root

        self.config=self._root.config
        self.log=self._root.log
        self.db=self._root.db

    def get_logs(self, page, project_name=None, log_level=None):
        limit=self.config.api.results_per_page
        skip=(int(page)-1)*limit

        logs=self.db.get_logs(
            limit=limit,
            skip=skip,
            project_name=project_name,
            log_level=log_level,
            )
        self.log.success('Obtained logs')

        return logs

    def create_logs_project(self, logs_project_name):
        if self.db.logs_project_exists(logs_project_name=logs_project_name):
            raise LogsProjectExists
        
        logs_project_uuid=uuid4()
        logs_project=self._db.create_logs_project(
            logs_project_name=logs_project_name,
            logs_project_uuid=logs_project_uuid
            )
        del logs_project['_id']  

        return logs_project
