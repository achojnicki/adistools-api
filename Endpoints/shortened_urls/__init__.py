from Message import Message

class shortened_urls:
    def shortened_urls(self, page=1, **kwargs):
        msg=Message()

        urls=self.middlewares.url_shortener.get_urls(
            page=page
            )
        
        msg.status="Success"
        msg.message="Shortened urls"
        msg.data=urls
        return msg