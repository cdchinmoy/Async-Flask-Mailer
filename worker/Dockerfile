FROM python:3

RUN pip install --upgrade pip  --no-cache-dir pika

WORKDIR /app

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]