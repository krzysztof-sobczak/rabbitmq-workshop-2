#!/usr/bin/env python
import pika
import time

## Implement consumption of message from "find-opponent" queue binded to "enter-game" exchange
## It should retry twice with delay of 5 seconds and then publish a message to "send-notification" exchange
## Documentation: https://www.rabbitmq.com/ttl.html