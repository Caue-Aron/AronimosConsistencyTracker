import datetime

class Day:
    def __init__(self):
        current_time = datetime.datetime.now()

        self.day = current_time.day
        self.month = current_time.month
        self.year = current_time.year

        self.success = 0
        self.fails = 0

    def add_success(self, amount):
        self.success += amount

    def add_fails(self, amount):
        self.fails += amount

    def get_date(self):
        value = (self.month, self.day, self.year)
        return value