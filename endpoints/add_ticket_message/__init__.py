from response import Response
from exceptions import TicketDoesntExists

class add_ticket_message:
	def add_ticket_message(self, ticket_uuid: str, ticket_message: str, session_uuid: str, **kwargs):
		try:
			rsp=Response()

			message=self._middlewares.tickets.add_ticket_message(
				ticket_uuid=ticket_uuid,
				session_uuid=session_uuid,
				message=ticket_message
				)
			rsp.status="Success"
			rsp.message="Message has been added to the ticket"
			rsp.data[ticket_uuid]=message

		except TicketDoesntExists:
			rsp.status="Error"
			rsp.message="Ticket doesn't exist."

		return rsp