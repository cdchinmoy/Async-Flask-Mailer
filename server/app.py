from flask import Flask, jsonify
import redis
import json
import time
import publisher

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379)

@app.route('/')
def index():
    return jsonify('OK'),200


@app.route('/create-job/<email>')
def add(email):
    r.incr('create_job', amount=1)
    publisher.publish(email)
    return jsonify("Job created Successfully!"),200
        
    
@app.route('/hits', methods=['GET'])
def hits():
    hits = int(r.get('create_job').decode('utf-8'))
    if hits:
        return json.dumps({'create_job': hits})
    else:
        return jsonify("No record!"),200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')