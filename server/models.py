# models.py
import os
from peewee import PostgresqlDatabase, Model, CharField, DateField

DATABASE = {
    'HOST': os.environ['DB_HOST'],
    'PORT': os.environ['DB_PORT'],
    'NAME': os.environ['DB_NAME'],
    'USER': os.environ['DB_USER'],
    'PASSWORD': os.environ['DB_PASSWORD'],
}

db = PostgresqlDatabase(
    DATABASE['NAME'], user=DATABASE['USER'], password=DATABASE['PASSWORD'], host=DATABASE['HOST'], port=DATABASE['PORT']
)


class Question(Model):
    question_text = CharField()
    pub_date = DateField()

    class Meta:
        database = db


class User(Model):
    name = CharField()
    email = CharField()
    phone = CharField()
    password = CharField()
    created_at = DateField()
    
    class Meta:
        database = db

if db.table_exists('question') is False:
    db.create_tables([Question])

if db.table_exists('user') is False:
    db.create_tables([User])    