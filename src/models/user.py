from mongoengine import Document, StringField, DateTimeField
import datetime

class User(Document):
    """
    TASK: Create a model for user with minimalistic
          information required for user authentication

    HINT: Do not store password as is.
    """
    user_id = StringField(max_length=200, required=True, unique=True)
    password  = StringField(max_length=200, required=True)
    date_created = DateTimeField(default=datetime.datetime.utcnow)

    def get_user_dict(self):
          user_dict = {}
          user_dict['user_id'] = self.user_id
          user_dict['date_created'] = self.date_created
          return user_dict

