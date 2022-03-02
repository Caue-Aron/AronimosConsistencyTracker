class Stage:
    def __init__(self, name):
        self.name = name
        self.success = 0
        self.fails = 0

    def get_name(self):
        return self.name

    def get_success(self):
        return self.success

    def get_fails(self):
        return self.fails

    def set_success(self, amount):
        self.success = amount

    def set_fails(self, amount):
        self.fails = amount

    def __iter__(self):
        yield from {
            'name':     self.name,
            'success':  self.success,
            'fails':    self.fails
        }
