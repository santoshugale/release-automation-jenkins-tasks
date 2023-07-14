FROM python:latest
WORKDIR /usr/src/app
RUN pip install pika
COPY DeleteRMQQueues.py ./
COPY QueuesList.csv ./
ENTRYPOINT ["python", "-u", "./DeleteRMQQueues.py"]
