class url_shortener:
    def get_urls(self, limit, skip):
        urls=[]
        cursor=self.shortened_urls.find().skip(skip).limit(limit)
        for item in cursor:
            urls.append(item)
        return urls

    def get_url(self, redirection_uuid: str):
        query={"redirection_uuid": redirection_uuid}

        url={}
        cursor=self.shortened_urls.find_one(query)
        if cursor:
            for item in cursor:
                url[item]=cursor[item]

        return url

    def get_url_by_query(self, redirection_query: str):
        query={"redirection_query": redirection_query}

        url={}
        cursor=self.shortened_urls.find_one(query)
        if cursor:
            for item in cursor:
                url[item]=cursor[item]

        return url

    def get_url_metrics(self, redirection_uuid: str):
        query={"redirection_uuid": redirection_uuid}
        
        metrics=[]
        cursor=self.shortened_urls_metrics.find(query)

        for item in cursor:
            metrics.append(item)

        return metrics

    def create_short_url(self, redirection_url: str, redirection_uuid: str, redirection_query: str):
        document={
            'redirection_url' : redirection_url,
            'redirection_uuid' : str(redirection_uuid),
            'redirection_query' : redirection_query  
        }

        self.shortened_urls.insert_one(document)
        return document

    def short_url_exists(self, redirection_query: str):
        return True if self.get_url_by_query(redirection_query=redirection_query) else False



