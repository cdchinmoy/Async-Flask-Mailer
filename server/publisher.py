import pika
import os

def publish(email):
    try:
        credentials = pika.PlainCredentials(os.environ['RABBITMQ_USER'], os.environ['RABBITMQ_PASS'])
        parameters =  pika.ConnectionParameters(os.environ['RABBITMQ_HOST'], credentials=credentials, heartbeat=5)
        connection = pika.BlockingConnection(parameters)

        channel = connection.channel()
        channel.queue_declare(queue='task_queue', durable=True)
        channel.basic_publish(
            exchange='',
            routing_key='task_queue',
            body=email,
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ))

        connection.close()
        
    except Exception as e:
        print("Failed to connect to RabbitMQ service. Message wont be sent.")