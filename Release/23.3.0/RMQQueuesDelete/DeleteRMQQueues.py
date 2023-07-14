import sys
import pika
import subprocess
import shlex
import csv

def run(cmd):
    return subprocess.check_output(shlex.split(cmd))

def get_queues():
    with open("QueuesList.csv") as queueList:
        reader_obj = csv.reader(queueList)
        for row in reader_obj:
            yield row[0]
    
def delete_queues():
    credentials = pika.PlainCredentials('guest', 'guest')
    pika.ConnectionParameters('localhost', 15672, "/", credentials)
    connection = pika.BlockingConnection() 
    
    for queue in get_queues():
        try:
            channel = connection.channel()
            print("Purging queue:- ", queue)
            channel.queue_purge(queue=queue)
            channel.queue_delete(queue=queue)
        except Exception as ex:
            print('unable to delete queue:- ', queue)
            print('ex-: ', ex)

    connection.close()

def main():
    try:
       print("Queues Deletion Started")
       delete_queues()
       print("Queues Deletion Completed")
    except Exception as ex:
        print(ex)

main()
