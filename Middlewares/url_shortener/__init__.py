from Exceptions import RedirectionQueryExists

from uuid import uuid4

class URL_shortener:
    def __init__(self, root):
        self._root=root

        self.config=self._root.config
        self.log=self._root.log
        self.db=self._root.db

    def get_urls(self, page):
        limit=self.config.api.results_per_page
        skip=(int(page)-1)*limit

        urls=self.db.get_urls(
            limit=limit,
            skip=skip
            )
        for item in urls:
            del item['_id']

        return urls

    def get_url(self, redirection_uuid: str, **kwargs):
        url=self.db.get_url(
            redirection_uuid=redirection_uuid
            )
        del url['_id']
        return url

    def get_url_metrics(self, redirection_uuid: str, **kwargs):
        metrics=self.db.get_url_metrics(
            redirection_uuid=redirection_uuid
            )
        for item in metrics:
            del item['_id']
        return metrics

    def create_short_url(self, redirection_url: str, redirection_query: str):
        if self.db.short_url_exists(redirection_query):
            raise RedirectionQueryExists

        redirection_uuid=uuid4()

        document=self.db.create_short_url(
            redirection_uuid=redirection_uuid,
            redirection_query=redirection_query,
            redirection_url=redirection_url
            )
        del document['_id']

        self.log.info('short url({redirection_query}) created for {redirection_url}')
        return document


