import datetime

class Day:
    def __init__(self):
        current_time = datetime.datetime.now()

        self.day = current_time.day
        self.month = current_time.month
        self.year = current_time.year

        self.success = 0
        self.fails = 0

day = Day()