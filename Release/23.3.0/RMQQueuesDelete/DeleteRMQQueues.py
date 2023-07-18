import pika
import csv
import sys
dict = {
        'dev1': 'rabbitmq-nlb.io.dev1.velocify.net', 
        'dev2': 'rabbitmq-nlb.io.dev2.velocify.net',
        'qa': 'rabbitmq-nlb.io.qa.velocify.net',
        'peg': 'rabbitmq-nlb.io.peg.velocify.net',
        'stg':'rabbitmq-nlb.io.stg.velocify.com',
        'stg2':'p-rabbitmq-nlb.io.stg.velocify.com',
        'prod':'rabbitmq-nlb.io.prod.velocify.com',
        'prod2':'p-rabbitmq-nlb.io.prod.velocify.com'
}
env = sys.argv[1]
host = dict[env]
print("Queues Deletion Started")
print("Environment:", env)
print("Host:", host)
credentials = pika.PlainCredentials('DialIq', sys.argv[2])
parameters = pika.ConnectionParameters(host, 5672, "/", credentials)
connection = pika.BlockingConnection(parameters)
with open("QueuesList.csv") as queueList:
    reader_obj = csv.reader(queueList)
    for row in reader_obj:
        try:
            channel = connection.channel()
            print("Purging queue:- ", row[0])
            channel.queue_purge(queue=row[0])
            channel.queue_delete(queue=row[0])
        except Exception as ex:
            print('unable to delete queue:- ', row[0])
            print('ex-: ', ex)        
connection.close()

print("Queues Deletion Completed")
