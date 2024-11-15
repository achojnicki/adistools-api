from response import Response

class tickets:
    def tickets(self, page=1, **kwargs):
        rsp=Response()

        tickets=self._middlewares.tickets.get_tickets(
            page=page
            )
        
        rsp.status="Success"
        rsp.message="Tickets"
        rsp.data=tickets
        return rsp