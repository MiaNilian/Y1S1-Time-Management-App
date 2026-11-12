# This file will create the Class "ActivityManager" for the time management app. The ActivityManager class is responsible for
# managing a collection of Activity objects, providing methods to add, remove, and retrieve activities.
import Activity
from ActivityKeeper import ActivityKeeper
class ActivityManager:

    def __init__(self):
        self.activities = [] # creates an empty list to store activities.
        self.next_id = 0 # stores the next ID value
        self.keeper = ActivityKeeper()

    def add_activity(self, activity):
        activity.id = self.next_id #assigns the class object with a unique ID
        self.next_id += 1 # increases the number of the next ID by 1 
        self.activities.append(activity) # appends the new activity class object to the list of activities 


    def find_activity_title(self, title): # intends to find the activity by title
        activity_titles = [activity for activity in self.activities if activity.title == title]  # finds all the class objects with the same title attribute, input 'title recieved from main code
        return activity_titles # returns the output 
        


    def find_activity_id(self, id):
        activity_id = [activity for activity in self.activities if activity.id == id] # does the same as the title one but for IDs
        return activity_id

    def find_activity_time(self, time):
        activity_time = [activity for activity in self.activities if activity.time == time] # does the same as the last two but for time.
        return activity_time 

    def find_activity_date(self, date):   
        activity_date = [activity for activity in self.activities if activity.date == date] # you know the drill by now 
        return activity_date

    def edit_activity(self, activity, value, edit): # takes the activity and value the user wants to edit and takes what the user wants to change it to
        setattr(activity, value, edit) # basically 'activity.value = edit", replacing the old value with the new one
        self.keeper.save(self.activities)


    def delete_activity(self, activity):
        self.activities.remove(activity)
        self.keeper.save(self.activities)