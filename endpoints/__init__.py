from endpoints import (
    login,
    logout,
    shortened_url,
    shortened_url_metrics,
    shortened_urls,
    create_short_url,
    logs,
    create_logs_project
    )

class Endpoints(login.login,
    logout.logout,
    shortened_url.shortened_url,
    shortened_url_metrics.shortened_url_metrics,
    shortened_urls.shortened_urls,
    create_short_url.create_short_url,
    logs.logs,
    create_logs_project.create_logs_project
    ):
    def __init__(self, root):
        self._root=root

        self._middlewares=root.middlewares
        self._log_handle=root.log_handle

        self._endpoints_with_required_login=[
            self.logout,
            self.shortened_url,
            self.shortened_urls,
            self.shortened_url_metrics,
            self.create_short_url,
            self.logs,
            self.create_logs_project
            ]