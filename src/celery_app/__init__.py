import logging
from celery import Celery
from models.login_history import LoginHistory
from utils.db_utils import connect_mongo
from utils.utils import str_to_date
from settings.local_settings import CELERY_SETTINGS
import time
def make_celery(app_name=__name__):
    return Celery(__name__, broker=CELERY_SETTINGS['CELERY_BROKER_URL'])

celery = make_celery()
connect_mongo()

@celery.task()
def record_last_login(user_id,last_login):
    new_login = LoginHistory(user_id, str_to_date(last_login))
    time.sleep(5)
    new_login.save()