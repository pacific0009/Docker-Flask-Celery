import hashlib
import datetime
from models.user import User
from utils.utils import date_to_str
from .service_error import *
class UserService():
    """
    service function for user related business logic
    """
    def login_user(self, credentials):
        """
        TASKS: write the logic here for user login
               authenticate user credentials as per your
               schema and return the identifier user.

               raise appropriate errors wherever necessary
        """
        password = hashlib.md5(credentials['password'].encode()).hexdigest()
        user = User.objects(user_id=credentials['user_id']).first()
        if not user:
            raise InvalidUser()
        if not user.password == password:
            raise InvalidCredentials()
        user =  user.get_user_dict()
        user['last_login'] = date_to_str(datetime.datetime.utcnow())
        return user 

