from uuid import uuid4
from hashlib import sha256

from API import config
from pymongo import MongoClient

admin_email="adrian@chojnicki.info"
admin_password="aa"






connection=MongoClient(
    host=config.mongo.host,
    port=config.mongo.port
    )

database=connection[config.mongo.db]

users=database['users']
trackers=database['pixel_trackers']


user_document={
    "user_uuid"    : str(uuid4()),
    "user_email"   : admin_email,
    "password_hash": sha256(admin_password.encode('utf-8')).hexdigest()
    }

users.insert_one(user_document)
