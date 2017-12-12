#!/usr/bin/env python
import pika
import time

## Implement consumption of message from "grant-reward-failure" queue handling failed messages from "grant-reward" queue via "deadletter" config
## The logic should publish a message to "send-notification" exchange
## Documentation: http://www.rabbitmq.com/dlx.html
