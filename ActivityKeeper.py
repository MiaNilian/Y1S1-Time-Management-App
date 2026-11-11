# This class is the Keeper of activities. it's responsibility is to save and load Activity class objects.
# it will take the activities from the manager, turn each activity into a dictionary and save them in A JSON file on the disk to keep a permanent save out of memory
# it will then load the JSON file and turn it into activity objects and pass them to the manager
import ActivityManager
import json
manager = ActivityManager()

def save(manager, activities):
    for activity in manager.activities:
        activity = {id: activity.id, title: activity.title, time: activity.time, date: activity.date}
        with open('activities.json', 'w') as file:
            json.dump(activity, 'activities.json', indent=4)
    

def load(manager, activities):
    with open('activities.json', 'r') as file:
        loaded_activities = json.load('activities.json')   
