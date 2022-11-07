import os
from google.cloud import pubsub_v1

credentials_path = '/PATH/TO/YOU/PRIVATE/JSON/FILE/HERE/myFile.privateKey.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path


publisher = pubsub_v1.PublisherClient()
topic_path = 'MY_TOPIC_NAME_HERE'


data = 'A garden sensor is ready!'
data = data.encode('utf-8')
attributes = {
    'sensorName': 'senseor001',
    'temperature': '75.0',
    'humidity': '60'
}

future = publisher.publish(topic_path, data, **attributes)
print(f'published message id {future.result()}')
