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

        self._config=self._root._config
        self._log=self._root._log

        self._mongo_cli=MongoClient(
            self._config.mongo.host,
            self._config.mongo.port,
        )

        self._db=self._mongo_cli[self._config.mongo.db]

        self._users=self._db['users']
        self._sessions=self._db['sessions']

        self._shortened_urls=self._db['shortened_urls']
        self._shortened_urls_metrics=self._db['shortened_urls_metrics']

        self._logs=self._db['logs']
        self._logs_projects=self._db['logs_projects']
        