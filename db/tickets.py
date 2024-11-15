class tickets:
    def get_tickets(self, limit, skip):
        tickets=[]
        cursor=self.tickets.find().skip(skip).limit(limit)
        for item in cursor:
            tickets.append(item)
        return tickets

    def get_ticket(self, ticket_uuid: str):
        query={"ticket_uuid": ticket_uuid}

        ticket={}
        cursor=self.tickets.find_one(query)
        if cursor:
            for item in cursor:
                ticket[item]=cursor[item]

        return ticket
 

    def get_ticket_messages(self, ticket_uuid: str):
        query={"ticket_uuid": ticket_uuid}
        
        messages=[]
        cursor=self.tickets_messages.find(query)

        for item in cursor:
            messages.append(item)

        return messages

    def create_ticket(self, ticket_uuid: str, ticket_title:str, user_uuid: str, ticket_timestamp: float):
        document={
            'ticket_uuid' : str(ticket_uuid),
            'ticket_title' : ticket_title,
            'user_uuid': user_uuid,
            'ticket_created_timestamp': ticket_timestamp,
            'ticket_last_modified_timestampt': ticket_timestamp
        }

        self.tickets.insert_one(document)
        return document

    def add_ticket_message(self, ticket_uuid: str, user_uuid: str, message_timestamp: float, message:str):
        document={
            'ticket_uuid' : str(ticket_uuid),
            'user_uuid': str(user_uuid),
            'message_timestamp': message_timestamp,
            'message' : message,
        }

        self.tickets_messages.insert_one(document)
        return document

    def ticket_exists(self, ticket_uuid: str):
        return True if self.get_ticket(ticket_uuid=ticket_uuid) else False

    def delete_ticket(self, ticket_uuid: str):
        document={"ticket_uuid": ticket_uuid}
        self.tickets.delete_one(document)
        self.tickets_messages.delete_many(document)
