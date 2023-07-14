import pika
import csv
 
print("Queues Deletion Started")
credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('20.85.124.141', 5672, "/", credentials)
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
