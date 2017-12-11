#!/usr/bin/env python
import pika
import time

## Implement consumption of message from "grant-reward" queue binded to "enter-game" exchange
## The logic should publish a message to "send-notification" exchange