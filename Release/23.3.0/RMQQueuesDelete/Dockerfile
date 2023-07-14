FROM python:latest
WORKDIR /usr/src/app
RUN pip install pika
COPY DeleteRMQQueues.py ./
COPY QueuesList.csv ./
CMD ["python", "-u", "DeleteRMQQueues.py"]
