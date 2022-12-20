import pulsar
import json
import sys
import requests
import time

topic = sys.argv[1] if len(sys.argv) > 0 else 'male'
topic = 'public/rbd/'+topic

client = pulsar.Client('pulsar://rbd-4:6650,rbd-5:6650,rbd-6:6650')
consumer = client.subscribe(topic, subscription_name='my-sub')

while True:
    msg = consumer.receive()
    data = json.loads(msg.data().decode('utf-8'))
    print("Received message: '%s'" % msg.data())
    
    headers = {
        'label': str(int(time.time())),
        'format': 'json'
    }
    print('received data')
    print(data)
    consumer.acknowledge(msg)

client.close()
