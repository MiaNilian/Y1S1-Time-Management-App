# This class is the Keeper of activities. it's responsibility is to save and load Activity class objects.
# it will take the activities from the manager, turn each activity into a dictionary and save them in A JSON file on the disk to keep a permanent save out of memory
# it will then load the JSON file and turn it into activity objects and pass them to the manager
from Activity import Activity
import json


class ActivityKeeper:

    def save(self, activities): # creates a save of the activity objects
        activities_list = []
        for activity in activities: # for each activity in the list, this loop creates a dictionary for each class object and stores it's values in a dict
            activitys = {'id': activity.id, 'title': activity.title, 'time': activity.time, 'date': activity.date}
            activities_list.append(activitys) # creates a list of the dicts
        with open('activities.json', 'w') as file: # opens the file with write permission
            json.dump(activities_list, file, indent=4) # dumps the dicts into a save file
    

    def load(self, manager): # loads the save file, turns it into activity objects and passes them to the manager where they get assigned new IDs
        with open('activities.json', 'r') as file: # opens the file with read permission
            loaded_activities = json.load(file) 
            for activitys in loaded_activities: 
                new_activity = Activity(activitys['title'], activitys['date'], activitys['time']) # turns each dict into a new activity class object
                manager.add_activity(new_activity) # passes it to the manager
