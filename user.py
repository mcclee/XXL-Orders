import DatabaseController
import config


class User:
    def __init__(self, ID, *args):
        self.orders = {}  # item id: counts
        self.user_id = ID
        self.name = args[0]
        self.address = args

    def pay(self):
        pass





