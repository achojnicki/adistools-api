from json import dumps
from pickle import NONE

class Message:
    type=None
    message=None
    data=None
    
    def __init__(self):
        self.type=None
        self.message=None
        self.data={}


    def __str__(self):
        return dumps({
            'type':self.type,
            'message':self.message,
            'data':self.data if len(self.data)>=1 else None
        },
        ensure_ascii=True)
        
    def __bytes__(self):
        return self.__str__().encode('utf-8')