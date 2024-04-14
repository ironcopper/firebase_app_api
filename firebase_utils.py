import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging,db

cred = credentials.Certificate("credentials_file.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://..........firebaseio.com" 
})

def saveToDb(latitude, longtitude, ripeness):
    ref = db.reference("notifications") #kütüphaneye bak(data bloğunu alıo)
    ref.push().set({
        "lat":latitude,
        "lot":longtitude,
        "ripeness":ripeness
    })

def sendTopicMessage(latitude, longtitude, ripeness):
    message = messaging.Message(
        notification=messaging.Notification(
            title="You have a new data",
            body="lat:{}, lot:{}, ripeness:{}".format(latitude, longtitude, ripeness) 
        ),
        topic="topicOfMessage",
    )
    messaging.send(message)

