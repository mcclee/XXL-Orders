from flask import Flask
from user import User
import config
import DatabaseController

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'


class ServerController:
    def __init__(self, app):
        self.database = DatabaseController.DBController(config.database_name)
        self.app = app
        self.users = {}

    def login(self, pairs):
        if self.authentication(pairs):
            ur = User()
            self.users.
            return True
        return False

if __name__ == '__main__':
    app.run()