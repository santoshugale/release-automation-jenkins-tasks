FROM python:latest
RUN pip install pika
COPY DeleteRMQQueues.py ./
COPY QueuesList.csv ./
ENTRYPOINT ["python", "./DeleteRMQQueues.py"]
