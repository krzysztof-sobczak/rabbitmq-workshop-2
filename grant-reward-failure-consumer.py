#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='message-broker'))
channel = connection.channel()

channel.queue_declare(queue='grant-reward-failed', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

channel.queue_bind(exchange='enter-game-failed', queue='grant-reward-failed')

def callback(ch, method, properties, body):
    channel.basic_publish(exchange='send-notification',
                              routing_key='',
                              body='Recovered reward for entering the game')

    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='grant-reward-failed',
                      on_message_callback=callback)

channel.start_consuming()