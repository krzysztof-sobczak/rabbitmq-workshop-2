#!/usr/bin/env python
import pika
import time
import requests
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='message-broker'))
channel = connection.channel()

channel.exchange_declare(exchange='send-notification',
                         exchange_type='fanout')

channel.queue_declare(queue='send-notification', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

channel.queue_bind(exchange='send-notification', queue='send-notification')

def callback(ch, method, properties, body):

    header = {"Content-Type": "application/json; charset=utf-8",
              "Authorization": "Basic MzFjOTc3MjEtYWFlOC00NGQ4LWJjYTYtNWQzOTQwYTI1ZjU0"}

    message = str(body)
    payload = {"app_id": "39ce40cf-9326-49ee-9fb3-b32c00828b37",
               "filters": [
    			  	{"field": "tag", "key": "userId", "relation": "=", "value": "ksobczak"}
    			],
               "contents": {"en": message}}

    req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))

    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='send-notification')

channel.start_consuming()