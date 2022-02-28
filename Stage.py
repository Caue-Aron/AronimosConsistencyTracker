from Day import Day

class Stage:
    def __init__(self, name='Untitled stage/mission'):
        self.days = list()
        self.name = name

    def get_name(self):
        return self.name

    def get_days(self):
        value = list.copy(self.days)
        return value

    def get_most_success_day(self):
        most = None
        for i in self.days:
            