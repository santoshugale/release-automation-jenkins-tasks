import pika
import csv
import sys
print("Environment:", sys.argv[1])
print("Host:", sys.argv[2])
print("User:", sys.argv[3])
print("Password:", sys.argv[3])

print("Queues Deletion Started")
credentials = pika.PlainCredentials(sys.argv[3], sys.argv[4])
parameters = pika.ConnectionParameters(sys.argv[2], 5672, "/", credentials)
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
