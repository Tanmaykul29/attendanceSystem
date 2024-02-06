import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://attendancespit-default-rtdb.firebaseio.com/'
})

ref = db.reference('Students')
data = {
    "321654": {
        "name": "Hassan",
        "major": "Robotics",
        "starting_year": 2017,
        "total_attendance": 25,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2023-11-28 00:54:34"
    },
    "852741": {
            "name": "Ellie",
            "major": "Robotics",
            "starting_year": 2018,
            "total_attendance": 15,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-11-28 00:54:34"
    },
    "963852": {
            "name": "Elon",
            "major": "Robotics",
            "starting_year": 2019,
            "total_attendance": 35,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-11-28 00:54:34"
    },
    "2021700033": {
            "name": "Tanmay Kulkarni",
            "major": "CSE - DS",
            "starting_year": 2022,
            "total_attendance": 35,
            "standing": "E",
            "year": 3,
            "last_attendance_time": "2023-11-28 00:54:34"
    },
}

for key,value in data.items():
    ref.child(key).set(value)