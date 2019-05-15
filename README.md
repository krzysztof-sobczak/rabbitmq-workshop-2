# RabbitMQ workshop vol.2

## Setup

Add to **/etc/hosts** (Linux) or **c:\WINDOWS\system32\drivers\etc\hosts** (Windows):
 ```text
127.0.0.1 rabbitmq.workshop.com
```

Update **./index.html** with your custom/unique userId:
 ```javascript
var workshopUserId = "yourCustomUserName";
```

## Usage

Starting the project:
```bash
docker-compose up -d
```

Accessing RabbitMQ management dashboard:
http://rabbitmq.workshop.com:15672
