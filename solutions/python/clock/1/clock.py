class Clock:
    def __init__(self, hour, minute):
        self.time = (hour*60 + minute) % 1440

    @property
    def hour(self):
        return (self.time//60) % 24

    @property
    def minute(self):
        return self.time % 60

    def __repr__(self):
        return f'Clock({self.hour}, {self.minute})'

    def __str__(self):
        return f'{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}'

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

    def __add__(self, minutes):
        self.time += minutes
        return self.__str__()

    def __sub__(self, minutes):
        self.time -= minutes
        return self.__str__()
