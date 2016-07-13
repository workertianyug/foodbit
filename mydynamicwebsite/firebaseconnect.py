from firebase import firebase
import json
import datetime

def connect():
    f = firebase.FirebaseApplication('https://foodbit.firebaseio.com', None)
    return f

def upload(data):
    f = connect()
    f.post('/foodinfo', data)
    result = f.get('/foodinfo', None)
    # print(json.dumps(result, sort_keys=True, indent=4))
    return True

def deleteFood(foodId):
    f = connect()
    f.delete('/foodinfo', 'foodId')
    return True
