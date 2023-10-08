from Exceptions import RedirectionQueryExists

from uuid import uuid4
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

    def get_url(self, redirection_uuid: str, **kwargs):
        url=self._db.get_url(
            redirection_uuid=redirection_uuid
            )
        del url['_id']
        return url

    def get_url_metrics(self, redirection_uuid: str, **kwargs):
        metrics=self._db.get_url_metrics(
            redirection_uuid=redirection_uuid
            )
        for item in metrics:
            del item['_id']
        return metrics

    def create_short_url(self, redirection_url: str, redirection_query: str):
        if self._db.short_url_exists(redirection_query):
            raise RedirectionQueryExists

        redirection_uuid=str(uuid4())

        document=self._db.create_short_url(
            redirection_uuid=redirection_uuid,
            redirection_query=redirection_query,
            redirection_url=redirection_url
            )
        del document['_id']
        return document