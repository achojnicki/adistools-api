from Message import Message

class shortened_urls:
    def shortened_urls(self, **kwargs):
        msg=Message()

        try:
            urls=self._url_shortener.get_urls()
            
            msg.status="Success"
            msg.message="Shortened urls"
            msg.data=urls
        except:
            msg.status="Error"
            msg.message="Unable to obtain URLs"
        return msg