from json import dumps

class Message:
    status=None
    message=None
    http_code=None
    data=None
    
    def __init__(self):
        self.status=None
        self.message=None
        self.http_code=None
        self.data={}

    def __str__(self):
        msg={}
        if self.status:
            msg['status']=self.status
        
        if self.message:
            msg['message']=self.message

        if self.data:
            msg['data']=self.data

        return dumps(msg,ensure_ascii=True)
        
    def __bytes__(self):
        return self.__str__().encode('utf-8')