# This file will create the Class "activity" for the time management app. The Activity class is responsible for
# storing single activities and their titles, times and dates, As well as validating the input of the user 
# to ensure that the activity is valid and can be stored in the database.

class Activity:
    def __init__(self, title, date, time):
        self.title = title
        self.date = date
        self.time = time
        if title == "":
            raise ValueError("Title cannot be empty")