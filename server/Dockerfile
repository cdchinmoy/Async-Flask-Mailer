FROM python:3

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --upgrade pip  --no-cache-dir -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]