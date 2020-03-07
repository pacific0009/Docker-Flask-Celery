from settings.local_settings import MONGO_SETTINGS
import mongoengine
def connect_mongo():
    mongoengine.connect(
        alias='default',
        db=MONGO_SETTINGS['DB_NAME'],
        host=MONGO_SETTINGS['DB_HOST'],
        port=MONGO_SETTINGS['DB_PORT'],
        username=MONGO_SETTINGS['DB_USERNAME'],
        password=MONGO_SETTINGS['DB_PASSWORD'],
    )