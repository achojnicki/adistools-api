from endpoints import (
    login,
    logout,
    shortened_url,
    shortened_url_metrics,
    shortened_urls,
    create_short_url,
    delete_short_url,
    logs,
    create_logs_project,
    pixel_tracker,
    pixel_trackers,
    pixel_tracker_metrics,
    create_pixel_tracker,
    delete_pixel_tracker,
    create_ticket,
    tickets,
    ticket,
    ticket_messages,
    add_ticket_message
    )

class Endpoints(login.login,
    logout.logout,
    shortened_url.shortened_url,
    shortened_url_metrics.shortened_url_metrics,
    shortened_urls.shortened_urls,
    create_short_url.create_short_url,
    delete_short_url.delete_short_url,
    logs.logs,
    create_logs_project.create_logs_project,
    pixel_tracker.pixel_tracker,
    pixel_trackers.pixel_trackers,
    pixel_tracker_metrics.pixel_tracker_metrics,
    create_pixel_tracker.create_pixel_tracker,
    delete_pixel_tracker.delete_pixel_tracker,
    create_ticket.create_ticket,
    tickets.tickets,
    ticket.ticket,
    ticket_messages.ticket_messages,
    add_ticket_message.add_ticket_message

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
            self.delete_short_url,
            self.logs,
            self.create_logs_project,
            self.pixel_tracker,
            self.pixel_trackers,
            self.pixel_tracker_metrics,
            self.create_pixel_tracker,
            self.delete_pixel_tracker,
            self.create_ticket,
            self.tickets,
            self.ticket,
            self.ticket_messages,
            self.add_ticket_message
            ]