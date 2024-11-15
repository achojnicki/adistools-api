from response import Response

class ticket:
    def ticket(self, ticket_uuid:str, **kwargs):
        rsp=Response()

        try:
            ticket=self._middlewares.tickets.get_ticket(
                ticket_uuid=ticket_uuid
                )
            rsp.status="Success"
            rsp.message="Ticket"
            rsp.data[ticket_uuid]=ticket
        except:
            rsp.status="Error"
            rsp.message="Unable to obtain ticket"
        return rsp