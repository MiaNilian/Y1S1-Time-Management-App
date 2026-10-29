# This file will create the Class "activity" for the time management app. The Activity class is responsible for
# storing single activities and their titles, times and dates.

class Activity:
    def __init__(self, title, date, time):
        self.title = title
        self.date = date
        self.time = time