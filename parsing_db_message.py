import firebase_admin
from firebase_admin import credentials,db,messaging

# Fetch the service account key JSON file contents
cred = credentials.Certificate('credentials_file.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://..........firebaseio.com"
})

def saveToDb(data):
    ref = db.reference("datas") 
    ref.push().set({
        "data":data,
    })

def sendTopicMessage(data):
    message = messaging.Message(
        notification=messaging.Notification(
            title="You have a new data",
            body="{}".format(data) 
        ),
        topic="topicOfMessage",
    )
    messaging.send(message)


def parsing_file(path):
    list = []

    with open(path, 'r') as file:
        for line in file:
            line = line.strip()

            if "X konumu:" in line and "Y konumu:" in line and "Olgunluk:" in line:

                x = line.split("X konumu:")[1].split("Y konumu:")[0].strip()
                y = line.split("Y konumu:")[1].split("Olgunluk:")[0].strip()
                o = line.split("Olgunluk:")[1].strip()

                if "+" in o:
                    o = o.replace("+", "ripe")
                elif "-" in o:
                    o = o.replace("-", "unripe")
                else:
                    o = o.replace("=", "nearly ripe")

                parsed_string = f"{o}({x}, {y})"
                list.append(parsed_string)

    return list


# Specifying file path
path = "fiile_path/data.txt"

result = parsing_file(path)

for i in result:
    sendTopicMessage(i)
    saveToDb(i)
