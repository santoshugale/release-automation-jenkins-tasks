FROM python:latest
WORKDIR /usr/src/app
RUN pip install pika
COPY UpdateUrls.py ./
COPY ClientList.csv ./
ENTRYPOINT ["python", "./UpdateUrls.py"]
