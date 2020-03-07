from mongoengine import Document, StringField, DateTimeField
import datetime

class LoginHistory(Document):
    """
        User login history
    """
    user_id = StringField(max_length=200, required=True)
    last_login = DateTimeField(required=True)

    def get_login_dict(self):
          user_dict = {}
          user_dict['user_id'] = self.user_id
          user_dict['last_login'] = self.last_login
          return user_dict

