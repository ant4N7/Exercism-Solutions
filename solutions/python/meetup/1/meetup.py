from datetime import timedelta
import calendar
CAL = calendar.Calendar()
WEEKDAY = {'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}
TEENTH = [13,14,15,16,17,18,19]
DELTAS = {'first':timedelta(),'second':timedelta(days=7),'third':timedelta(days=14),
          'fourth':timedelta(days=21),'fifth':timedelta(days=28),'last':timedelta(days=-7)}


class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date."""
    def __init__(self,message):
        self.message = message


def meetup(year, month, week, day_of_week):
    if week == 'teenth':
        for date in CAL.itermonthdates(year,month):
            if date.weekday() == WEEKDAY[day_of_week] and date.day in TEENTH:
                return date

    if week == 'last':
        next_month = month+1 if month < 12 else 1
        if next_month == 1: year += 1
        print(f'month:{month} next_month:{next_month} year:{year}')
        for date in CAL.itermonthdates(year,next_month):
            if date.month != next_month: continue
            if date.weekday() == WEEKDAY[day_of_week]:
                date += DELTAS[week]
                if date.month == month:
                    return date

    for date in CAL.itermonthdates(year,month):
        if date.month != month: continue
        if date.weekday() == WEEKDAY[day_of_week]:
            date += DELTAS[week]
            if date.month == month:
                return date

    raise MeetupDayException('That day does not exist.')
