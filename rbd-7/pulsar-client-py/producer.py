import pandas as pd
import time
import sys
from random import randrange
import pulsar
from clean_data import clean_genders

ENDLESS = int(sys.argv[1])
ADD_DELAY = int(sys.argv[2])
if ADD_DELAY == 1:
    MIN_DELAY = int(sys.argv[3])
    MAX_DELAY = int(sys.argv[4])

df = pd.read_csv('survey.csv')
df = clean_genders(df)
df = df.drop(['Timestamp'], axis=1)
df.insert(0, 'ID', range(0, len(df)))

# Pulsar Producer
pulsar_client = pulsar.Client('pulsar://rbd-4:6650,rbd-5:6650,rbd-6:6650')
producer_male = pulsar_client.create_producer('public/rbd/male')
producer_female = pulsar_client.create_producer('public/rbd/female')
producer_other = pulsar_client.create_producer('public/rbd/other')




while True:
    for index, row in df.iterrows():
        if ADD_DELAY == 1:
            time.sleep(randrange(MIN_DELAY, MAX_DELAY+1)/1000)
        row['Time'] = int(time.time())
        print(row.to_string())
        if row['Gender'] == 'male':
            producer_male.send(row.to_json().encode('utf-8'))
        if row['Gender'] == 'female':
            producer_female.send(row.to_json().encode('utf-8'))
        if row['Gender'] == 'other':
            producer_other.send(row.to_json().encode('utf-8'))
    if ENDLESS != 1:
        break
