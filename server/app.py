from flask import Flask, jsonify
import pika
import redis
import json
import time

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379)

@app.route('/')
def index():
    return jsonify('OK'),200


@app.route('/create-job/<email>')
def add(email):
    r.incr('create_job', amount=1)
    try:
        credentials = pika.PlainCredentials('root', 'root')
        parameters =  pika.ConnectionParameters('rabbitmq', credentials=credentials, heartbeat=5)
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

        return jsonify("Job created Successfully!"),200
        
    except Exception as e:
        print("Failed to connect to RabbitMQ service. Message wont be sent.")

    
@app.route('/hits', methods=['GET'])
def hits():
    hits = int(r.get('create_job').decode('utf-8'))
    if hits:
        return json.dumps({'create_job': hits})
    else:
        return jsonify("No record!"),200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')