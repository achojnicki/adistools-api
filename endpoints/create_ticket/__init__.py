from response import Response
from exceptions import TicketDoesntExists

class create_ticket:
	def create_ticket(self, ticket_title: str, ticket_message: str, session_uuid: str, **kwargs):
		rsp=Response()

		ticket=self._middlewares.tickets.create_ticket(
			ticket_title=ticket_title,
			session_uuid=session_uuid
			)

		message=self._middlewares.tickets.add_ticket_message(
			ticket_uuid=ticket['ticket_uuid'],
			session_uuid=session_uuid,
			message=ticket_message
			)
		rsp.status="Success"
		rsp.message="Ticket has been created."
		rsp.data[ticket['ticket_uuid']]=ticket

		return rsp