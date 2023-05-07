class url_shortener:
    def get_urls(self):
        urls=[]
        cursor=self._shortened_urls.find()
        for item in cursor:
            urls.append(item)
        return urls

    def get_url(self, url_uuid: str):
        query={"url_uuid": url_uuid}

        url={}
        cursor=self._shortened_urls.find_one(query)
        for item in cursor:
            url[item]=cursor[item]

        return url

    def get_url_metrics(self, url_uuid: str):
        query={"url_uuid": url_uuid}
        
        metrics=[]
        cursor=self._shortened_urls_metrics.find(query)

        for item in cursor:
            metrics.append(item)

        return metrics