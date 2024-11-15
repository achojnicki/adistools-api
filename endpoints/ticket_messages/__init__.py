from response import Response

class ticket_messages:
    def ticket_messages(self, ticket_uuid:str, **kwargs):
        rsp=Response()

        try:
            ticket_messages=self._middlewares.tickets.get_ticket_messages(
                ticket_uuid=ticket_uuid
                )
            rsp.status="Success"
            rsp.message="Ticket messages"
            rsp.data[ticket_uuid]=ticket_messages
        except:
            rsp.status="Error"
            rsp.message="Unable to obtain ticket messages"
        return rsp