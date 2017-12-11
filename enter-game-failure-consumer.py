#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='message-broker'))
channel = connection.channel()

channel.queue_declare(queue='grant-reward', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

channel.queue_bind(exchange='enter-game', queue='grant-reward')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='grant-reward')

channel.start_consuming()