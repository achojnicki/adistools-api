from exceptions import RedirectionQueryExists, RedirectionQueryDoesntExists

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

        urls={}
        data=self.db.get_urls(
            limit=limit,
            skip=skip
            )
        for item in data:
            del item['_id']

        for url in data:
            urls[url['redirection_uuid']]=url
        self.log.success('Obtained details about a short URLs')

        return urls

    def get_url(self, redirection_uuid: str):
        url=self.db.get_url(
            redirection_uuid=redirection_uuid
            )
        del url['_id']
        self.log.success('Obtained details about a short URL')
        return url

    def get_url_metrics(self, redirection_uuid: str):
        metrics=self.db.get_url_metrics(
            redirection_uuid=redirection_uuid
            )
        for item in metrics:
            del item['_id']
        self.log.success('Obtained metrics of short URL')
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

        self.log.success(f'Short url({redirection_query}) created for {redirection_url}')
        return document

    def delete_short_url(self, redirection_uuid: str):
        if not self.db.get_url(redirection_uuid):
            raise RedirectionQueryDoesntExists

        self.db.delete_short_url(redirection_uuid)


