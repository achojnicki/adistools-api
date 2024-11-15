from exceptions import TicketDoesntExists

from uuid import uuid4
from datetime import datetime

class Tickets:
    def __init__(self, root):
        self._root=root

        self.config=self._root.config
        self.log=self._root.log
        self.db=self._root.db

    def get_tickets(self, page):
        limit=self.config.api.results_per_page
        skip=(int(page)-1)*limit

        tickets={}
        data=self.db.get_tickets(
            limit=limit,
            skip=skip
            )
        for item in data:
            del item['_id']

        for ticket in data:
            user=self.db.get_user_by_user_uuid(ticket['user_uuid'])
            del user['_id']
            del user['password_hash']
            del ticket['user_uuid']
            ticket['user']=user
            tickets[ticket['ticket_uuid']]=ticket

        self.log.success('Obtained tickets.')

        return tickets

    def get_ticket(self, ticket_uuid: str):
        ticket=self.db.get_ticket(
            ticket_uuid=ticket_uuid
            )
        del ticket['_id']
        user=self.db.get_user_by_user_uuid(ticket['user_uuid'])
        del user['_id']
        del user['password_hash']
        del ticket['user_uuid']
        ticket['user']=user
        self.log.success(f"Obtained ticket({ticket['ticket_uuid']}, {ticket['ticket_title']})")
        return ticket

    def get_ticket_messages(self, ticket_uuid: str):
        ticket=self.db.get_ticket(ticket_uuid)

        messages=self.db.get_ticket_messages(
            ticket_uuid=ticket_uuid
            )
        for item in messages:
            user=self.db.get_user_by_user_uuid(item['user_uuid'])
            del user['_id']
            del user['password_hash']
            del item['user_uuid']
            item['user']=user
            del item['_id']
        self.log.success(f"Obtained messages of a ticket({ticket['ticket_uuid']}, {ticket['ticket_title']})")
        return messages

    def create_ticket(self, ticket_title: str, session_uuid: str):
        ticket_uuid=uuid4()
        creation_timestamp=datetime.now().timestamp()

        session=self.db.get_session_by_session_uuid(
            session_uuid=session_uuid)

        document=self.db.create_ticket(
            ticket_uuid=ticket_uuid,
            ticket_title=ticket_title,
            user_uuid=session['user_uuid'],
            ticket_timestamp=creation_timestamp
            )
        del document['_id']

        self.log.success(f"Ticket({ticket_uuid}, {ticket_title}) created.")
        return document

    def add_ticket_message(self, ticket_uuid: str, session_uuid: str, message:str):
        message_timestamp=datetime.now().timestamp()

        session=self.db.get_session_by_session_uuid(
            session_uuid=session_uuid)

        ticket=self.db.get_ticket(
            ticket_uuid=ticket_uuid
            )

        user=self.db.get_user_by_user_uuid(session['user_uuid'])
        del user['_id']
        del user['password_hash']

        if not ticket:
            raise TicketDoesntExists

        document=self.db.add_ticket_message(
            ticket_uuid=ticket_uuid,
            user_uuid=session['user_uuid'],
            message_timestamp=message_timestamp,
            message=message
            )
        del document['_id']
        del document['user_uuid']

        document['user']=user

        self.log.success(f"Message to the ticket({ticket_uuid}, {ticket['ticket_title']}) added.")
        return document


    def delete_ticket(self, ticket_uuid: str):
        ticket=self.db.get_ticket(ticket_uuid)
        if not ticket:
            raise TicketDoesntExists

        self.db.delete_ticket(ticket_uuid)
        self.log.success(f"Ticket({ticket['ticket_uuid']}, {ticket['ticket_title']}) has ben removed.")


