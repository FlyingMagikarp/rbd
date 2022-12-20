import pulsar
import json
import sys
import requests
import time

gender = sys.argv[1] if len(sys.argv) > 0 else 'male'
topic = 'public/rbd/'+gender

client = pulsar.Client('pulsar://rbd-4:6650,rbd-5:6650,rbd-6:6650')
consumer = client.subscribe(topic, subscription_name='my-sub')

while True:
    msg = consumer.receive()
    data = json.loads(msg.data().decode('utf-8'))
    print("Received message: '%s'" % msg.data())
    
    headers = {
        'label': str(hash(str(data)+str(int(time.time())))),
        'format': 'json'
    }


    response = requests.put('http://rbd-9:8040/api/rbd/answer_'+gender+'/_stream_load', headers=headers, data=msg.data(), auth=('root', ''))
    print(response.content)
    consumer.acknowledge(msg)

client.close()
