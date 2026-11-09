# This file will create the Class "ActivityManager" for the time management app. The ActivityManager class is responsible for
# managing a collection of Activity objects, providing methods to add, remove, and retrieve activities.
import Activity

class ActivityManager:

    def __init__(self):
        self.activities = [] # creates an empty list to store activities.
        self.next_id = 0 # stores the next ID value

    

    def add_activity(self, activity):
        activity.id = self.next_id #assigns the class object with a unique ID
        self.next_id += 1 # increases the number of the next ID by 1 
        self.activities.append(activity) # appends the new activity class object to the list of activities 


    def find_acvtivity_title():

    def find_activity_id():

    def find_activity_time():
    
    def find_activity_date():   

    def delete_activity():

    def edit_activity():