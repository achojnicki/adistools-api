class URL_shortener:
    def __init__(self, root):
        self._root=root
        self._log=self._root._log
        
        self._db=self._root._db

    def get_urls(self):
        urls=self._db.get_urls()
        for item in urls:
            del item['_id']

        return urls

    def get_url(self, url_uuid: str, **kwargs):
        url=self._db.get_url(
            url_uuid=url_uuid
            )
        del url['_id']
        return url

    def get_url_metrics(self, url_uuid: str, **kwargs):
        metrics=self._db.get_url_metrics(
            url_uuid=url_uuid
            )
        for item in metrics:
            del item['_id']
        return metrics