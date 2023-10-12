class Logs:
    def __init__(self, root):
        self._root=root

        self._config=self._root._config
        self._log=self._root._log
        self._db=self._root._db

    def get_logs(self, page):
        limit=self._config.api.results_per_page
        skip=(int(page)-1)*limit

        logs=self._db.get_logs(
            limit=limit,
            skip=skip
            )
        for item in logs:
            del item['_id']

        return logs
    def get_logs_by_project_name(self, project_name, page):
        limit=self._config.api.results_per_page
        skip=(int(page)-1)*limit

        logs=self._db.get_logs_by_project_name(
            project_name=project_name,
            limit=limit,
            skip=skip
            )

        for item in logs:
            del item['_id']

        return logs