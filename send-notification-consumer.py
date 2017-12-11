#!/usr/bin/env python
import pika
import time
import requests
import json

## Set correct value of userId to support notifications
userId = "ksobczak"

## Implement consumption of messages from "send-notification" queue binded to "send-notification" exchange

## Callback for sending notifications
def callback(ch, method, properties, body):

    header = {"Content-Type": "application/json; charset=utf-8",
              "Authorization": "Basic MzFjOTc3MjEtYWFlOC00NGQ4LWJjYTYtNWQzOTQwYTI1ZjU0"}

    message = str(body)
    payload = {"app_id": "39ce40cf-9326-49ee-9fb3-b32c00828b37",
               "filters": [
    			  	{"field": "tag", "key": "userId", "relation": "=", "value": userId}
    			],
               "contents": {"en": message}}

    req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))

    ch.basic_ack(delivery_tag = method.delivery_tag)