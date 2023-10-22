class logs:
    def get_logs(self, limit, skip, project_name:None, log_level=None):
        logs=[]
        query={}

        if project_name:
            query['project_name']=project_name
        if log_level:
            query['log_level']=log_level


        cursor=self.logs.find(query).skip(skip).limit(limit)
        for item in cursor:
            logs.append(item)
            del item['_id']
        
        return logs

    def create_logs_project(self, logs_project_name, logs_project_uuid):
        document={
            "logs_project_name": logs_project_name,
            "logs_project_uuid": str(logs_project_uuid)
        }

        self.logs_projects.insert_one(document)
         
        return document

    def get_logs_projects(self, limit, skip):
        logs_projects=[]
        cursor=self.logs_projects.find().skip(skip).limit(limit)
        for item in cursor:
            logs_projects.append(item)
        return logs_projects

    def get_logs_project(self, logs_project_uuid: str):
        query={"logs_project_uuid": log_project_uuid}

        logs_project={}
        cursor=self.logs_projects.find_one(query)
        if cursor:
            for item in cursor:
                logs_project[item]=cursor[item]

        return logs_project

    def get_logs_project_by_name(self, logs_project_name: str):
        query={"logs_project_name": logs_project_name}

        logs_project={}
        cursor=self.logs_projects.find_one(query)

        if cursor:
            for item in cursor:
                logs_project[item]=cursor[item]

        return logs_project

    def logs_project_exists(self, logs_project_name: str):
        return True if self.get_logs_project_by_name(logs_project_name=logs_project_name) else False
