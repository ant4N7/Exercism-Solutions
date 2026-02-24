class Clock:
    def __init__(self, hour, minute):
        if not isinstance(hour, int) or not isinstance(minute, int):
            raise TypeError("Hour and minute must be integers")
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
        return f'{self.hour:02d}:{self.minute:02d}'

    def __eq__(self, other):
        if isinstance(other, Clock):
            return self.time == other.time
        return False

    def __add__(self, minutes):
        self.time = (self.time + minutes) % 1440
        return self.__str__()

    def __sub__(self, minutes):
        return self.__add__(-minutes)
