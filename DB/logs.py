class logs:
    def get_logs(self, limit, skip):
        urls=[]
        
        cursor=self._logs.find().skip(skip).limit(limit)
        for item in cursor:
            urls.append(item)
        
        return urls

    def get_logs_by_project_name(self, project_name, limit, skip):
        urls=[]
        document={
            "project_name": project_name
        }

        cursor=self._logs.find(document).skip(skip).limit(limit)
        for item in cursor:
            urls.append(item)
        
        return urls