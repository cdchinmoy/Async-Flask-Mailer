# Asynchronous mail sneding using Flask, Rabbitmq, Redis, PostgreSQL
ENDPOINT 1:   <br/>
  Method: GET <br/>
  Descriription: Get all registration <br/>
  http://localhost:5000/user/registration <br/><br/>
  
  Method: POST  <br/>
  Descriription: New registration <br/>
  http://localhost:5000/user/registration <br/>
  Payload:  <br/>
  { <br/>
    "name":"Chinmoy Das", <br/>
    "email":"cdchinmoy@gmail.com",  <br/>
    "phone":"1234567890", <br/>
    "password":"123456" <br/>
  } <br/>
  Payload Type: JSON (application/json) <br/><br/>

## Get the number of hit count: <br/>
ENDPOINT 2: http://localhost:5000/hits  <br/><br/>

## Docker Compose Commend:  <br/>
docker-compose up --build
