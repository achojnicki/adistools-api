from response import Response

class shortened_urls:
    def shortened_urls(self, page=1, **kwargs):
        rsp=Response()

        urls=self._middlewares.url_shortener.get_urls(
            page=page
            )
        
        rsp.status="Success"
        rsp.message="Shortened urls"
        rsp.data=urls
        return rsp