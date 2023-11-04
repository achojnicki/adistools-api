from response import Response

class shortened_url:
    def shortened_url(self, redirection_uuid:str, **kwargs):
        rsp=Response()

        try:
            url=self._middlewares.url_shortener.get_url(
                redirection_uuid=redirection_uuid
                )
            rsp.status="Success"
            rsp.message="Shortened URL"
            rsp.data[redirection_uuid]=url
        except:
            rsp.status="Error"
            rsp.message="Unable to obtain URL"
        return rsp