#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='message-broker'))
channel = connection.channel()

channel.exchange_declare(exchange='enter-game',
                         exchange_type='fanout')

channel.basic_publish(exchange='enter-game',
                      routing_key='',
                      body='Entered game')

print(" [x] Sent enter-game message")

connection.close()
