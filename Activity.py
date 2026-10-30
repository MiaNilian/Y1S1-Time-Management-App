# This file will create the Class "activity" for the time management app. The Activity class is responsible for
# storing single activities and their titles, times and dates, As well as validating the input of the user 
# to ensure that the activity is valid and can be stored in the database.
# the class first recives input, then validates that input before storing it inside a class object.
from datetime import datetime


class Activity:
    def __init__(self, title, date, time): # initializes the class I guess
        if title == "": # checks to make sure the title isn't empty
                    raise ValueError("Title cannot be empty") # returns an error if invalid
        self.validate_date(date) # calls the validate_date function to check if the date is valid
        self.validate_time(time) # calls the validate_time function to check if the time is valid
        self.title = title
        self.date = date
        self.time = time
        
        
    def validate_date(self, date): # function to validate the date input by the user
        try:
            datetime.strptime(date, '%d/%m/%Y') # checks to make sure the date is in the correct format
            
        except ValueError:
            raise ValueError("Incorrect date format, should be DD/MM/YYYY") # returns an error if invalid

    def validate_time(self, time): # function to validate the time input by the user
        try:
            datetime.strptime(time, '%H:%M') # checks to make sure the time is in the correct format
            
        except ValueError:
            raise ValueError("Incorrect time format, should be HH:MM") # returns an error if invalid
