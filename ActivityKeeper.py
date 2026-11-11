# This class is the Keeper of activities. it's responsibility is to save and load Activity class objects.
# it will take the activities from the manager, turn each activity into a dictionary and save them in A JSON file on the disk to keep a permanent save out of memory
# it will then load the JSON file and turn it into activity objects and pass them to the manager
import ActivityManager
manager = ActivityManager()

def save(activities):
    for activity in manager.activities:
        activity = {id: activity.id, title: activity.title, time: activity.time, date: activity.date}
    

def load(activities)
