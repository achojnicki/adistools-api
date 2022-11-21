from .users import users
from .sessions import sessions
from .pixel_tracking import pixel_tracking


from pymongo import MongoClient

class DB(
    users,
    sessions,
    pixel_tracking
):
    def __init__(self, root):
        self._root=root

        self._config=self._root._config

        self._mongo_cli=MongoClient(
            self._config.mongo.host,
            self._config.mongo.port
        )

        self._db=self._mongo_cli[self._config.mongo.db]

        self._users=self._db['users']
        self._sessions=self._db['sessions']
        
        self._pixel_trackers=self._db['pixel_trackers']
        self._pixel_trackers_metrics=self._db['pixel_trackers_metrics']
        
        