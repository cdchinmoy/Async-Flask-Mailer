# Flask Asynchronous Email Service

This project demonstrates an asynchronous email-sending service using Flask, RabbitMQ, Redis, and PostgreSQL.

## Features

- **User Registration**: Register new users with their details.
- **Asynchronous Mail Sending**: Sends a confirmation email after registration using RabbitMQ as the message broker and Redis as the task queue backend.
- **Hit Count**: Tracks and displays the number of API hits.


## Installation and Setup

### Prerequisites
- Docker and Docker Compose installed on your system.

### Steps to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo.git
   cd your-repo
   ```

2. Build and run the application using Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. Access the application:
   - **API Base URL**: `http://localhost:5000`

---

## API Endpoints

### 1. **Get All Registrations**
   - **Method**: `GET`
   - **Endpoint**: `/user/registration`
   - **Description**: Retrieves all registered users.
   - **URL**: `http://localhost:5000/user/registration`


### 2. **New Registration**
   - **Method**: `POST`
   - **Endpoint**: `/user/registration`
   - **Description**: Registers a new user and sends an asynchronous confirmation email.
   - **URL**: `http://localhost:5000/user/registration`
   - **Payload**:
     ```json
     {
       "name": "Chinmoy Das",
       "email": "cdchinmoy@gmail.com",
       "phone": "1234567890",
       "password": "123456"
     }
     ```
   - **Payload Type**: `JSON` (`application/json`)


### 3. **Hit Count**
   - **Method**: `GET`
   - **Endpoint**: `/hits`
   - **Description**: Returns the number of times the API has been hit.
   - **URL**: `http://localhost:5000/hits`

---

## Architecture

1. **Flask**: Serves as the main application framework.
2. **RabbitMQ**: Acts as the message broker for asynchronous task processing.
3. **Redis**: Functions as the task queue backend.
4. **PostgreSQL**: Used as the primary database for user registration data.


## Environment Variables
Ensure the `.env` file is present in the root directory and contains the following variables:

```env
FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=postgresql://user:password@db:5432/yourdatabase
RABBITMQ_URL=amqp://user:password@rabbitmq:5672/
REDIS_URL=redis://redis:6379/0
```

Replace `user`, `password`, and `yourdatabase` with appropriate values.


## Testing
Test the endpoints using tools like **Postman**, **cURL**, or a browser for GET requests.


## Docker Compose
The `docker-compose.yml` orchestrates the services:
- `Flask` application
- `RabbitMQ`
- `Redis`
- `PostgreSQL`

To start all services:
```bash
docker-compose up --build
```

To stop and remove services:
```bash
docker-compose down
```


Feel free to contribute and enhance this project!
