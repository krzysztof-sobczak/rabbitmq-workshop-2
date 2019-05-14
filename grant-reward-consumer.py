#!/usr/bin/env python
import pika
import time
import requests
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='message-broker'))
channel = connection.channel()

channel.exchange_declare(exchange='enter-game',
                         exchange_type='fanout')

channel.exchange_declare(exchange='enter-game-failed',exchange_type='fanout')

channel.queue_declare(queue='grant-reward', durable = True, exclusive = False, auto_delete = False, arguments={
                                               "x-dead-letter-exchange" : "enter-game-failed",
                                             })
print(' [*] Waiting for messages. To exit press CTRL+C')

channel.queue_bind(exchange='enter-game', queue='grant-reward');

def callback(ch, method, properties, body):

    channel.basic_publish(exchange='send-notification',
                          routing_key='',
                          body='Received reward for entering the game')

    ch.basic_reject(delivery_tag = method.delivery_tag, requeue = False)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='grant-reward',
                      on_message_callback=callback)

channel.start_consuming()