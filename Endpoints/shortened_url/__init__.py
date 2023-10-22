from Message import Message

class shortened_url:
    def shortened_url(self, redirection_uuid:str, **kwargs):
        msg=Message()

        try:
            url=self._middlewares.url_shortener.get_url(
                redirection_uuid=redirection_uuid
                )
            msg.status="Success"
            msg.message="Shortened URL"
            msg.data[redirection_uuid]=url
        except:
            msg.status="Error"
            msg.message="Unable to obtain URL"
        return msg