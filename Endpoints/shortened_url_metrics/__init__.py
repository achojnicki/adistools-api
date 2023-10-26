from Response import Response

class shortened_url_metrics:
    def shortened_url_metrics(self, redirection_uuid: str, **kwargs):
        rsp=Response()

        try:
            metrics=self._middlewares.url_shortener.get_url_metrics(
                redirection_uuid=redirection_uuid
                )
            rsp.status="Success"
            rsp.message="Metrics for shortened URL"
            rsp.data[redirection_uuid]=metrics
        
        except:
            rsp.status="Error"
            rsp.message="Unable to obtain metrics for specific URL"
        return rsp