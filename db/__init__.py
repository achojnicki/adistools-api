from .users import users
from .sessions import sessions
from .url_shortener import url_shortener
from .logs import logs


from pymongo import MongoClient

class DB(
    users,
    sessions,
    url_shortener,
    logs

):
    def __init__(self, root):
        self._root=root

        self.config=self._root.config
        self.log=self._root.log

        self._mongo_cli=MongoClient(
            self.config.mongo.host,
            self.config.mongo.port,
        )

        self._db=self._mongo_cli[self.config.mongo.db]

        self.users=self._db['users']
        self.sessions=self._db['sessions']

        self.shortened_urls=self._db['shortened_urls']
        self.shortened_urls_metrics=self._db['shortened_urls_metrics']

        self.logs=self._db['logs']
        self.logs_projects=self._db['logs_projects']
        