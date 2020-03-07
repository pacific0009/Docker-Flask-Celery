import click
from models.user import User
from models.login_history import LoginHistory
import hashlib

@click.command()
@click.option('-u', default='root', help='user name')
@click.option('-p', default='root', help='password')
def createuser(u, p):
    # Create user code
    print("Creating the user")
    user_id = u
    password = hashlib.md5(p.encode()).hexdigest()
    if User.objects(user_id=u).first():
        print("user: {} alredy exist".format(u))
        return
    new_user = User(user_id=user_id, password=password)
    new_user.save()
    print("User Created")
    print(new_user.get_user_dict())

@click.command()
def showloginhistory():
    loginHistory = LoginHistory.objects().all()
    if not loginHistory:
        print("No entry found")
        return
    print("Total records: {}".format(loginHistory.count()))
    curser = max(0, loginHistory.count() - 50) 
    for history in loginHistory[curser:]:
        print(history.get_login_dict())