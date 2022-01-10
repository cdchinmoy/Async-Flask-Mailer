from flask import Flask, jsonify, request
import redis
import json
import time
from datetime import datetime, date
from publisher import publish
from models import Question, User

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379)

@app.route('/')
def index():
    return jsonify('OK'),200  


@app.route('/user/registration', methods=['GET','POST'])
def registration():
    r.incr('registration_hits', amount=1)
    if request.method == 'POST':
        name = request.json['name']
        email = request.json['email']
        phone = request.json['phone']
        password = request.json['password']
        today = date.today()
        user = User(name=name, email=email, phone=phone, password=password, created_at=today)
        user.save()
        # Mail
        recevier,subject,body = email,"Registration Successful!","Thank you for registering with us!"
        data = {'recevier':recevier, 'subject':subject, 'body':body}
        publish(data)
        
        rep = {'name': user.name, 'id': user.id, 'email': user.email, 'phone': user.phone}
        return jsonify(rep), 200

    elif request.method == 'GET':
        users = User.select()
        l = []
        for user in users:
            l.append({'name': user.name, 'id': user.id, 'email': user.email, 'phone': user.phone})
        return jsonify(l), 200

        
    
@app.route('/hits', methods=['GET'])
def hits():
    hits = int(r.get('registration_hits').decode('utf-8'))
    if hits:
        return json.dumps({'registration': hits})
    else:
        return jsonify("No record!"),200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')