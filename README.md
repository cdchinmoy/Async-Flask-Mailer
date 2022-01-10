# Asynchronous mail sneding using Flask, Rabbitmq, Redis, Postgres
ENDPOINT 1:   <br/>
  Method: GET <br/>
  Descriription: Get all registration
  http://localhost:5000/user/registration
  
  Method: POST
  Descriription: New registration
  http://localhost:5000/user/registration
  Payload:
  {
    "name":"Chinmoy Das",
    "email":"cdchinmoy@gmail.com",
    "phone":"1234567890",
    "password":"123456"
  }
  Payload Type: JSON (application/json)

## Get the number of hit count:
ENDPOINT 2: http://localhost:5000/hits


## Docker Compose Commend:
docker-compose up --build
