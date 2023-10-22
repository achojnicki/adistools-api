from Message import Message

class shortened_url_metrics:
    def shortened_url_metrics(self, redirection_uuid: str, **kwargs):
        msg=Message()

        try:
            metrics=self._middlewares.url_shortener.get_url_metrics(
                redirection_uuid=redirection_uuid
                )
            msg.status="Success"
            msg.message="Metrics for shortened URL"
            msg.data[redirection_uuid]=metrics
        
        except:
            msg.status="Error"
            msg.message="Unable to obtain metrics for specific URL"
        return msg