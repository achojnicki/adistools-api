from API.Endpoints import (
    login,
    logout,
    shortened_url,
    shortened_url_metrics,
    shortened_urls,
    create_short_url
    )

class Endpoints(login.login,
    logout.logout,
    shortened_url.shortened_url,
    shortened_url_metrics.shortened_url_metrics,
    shortened_urls.shortened_urls,
    create_short_url.create_short_url
    ):
    pass


    
