#!/usr/bin/env python

import pika

params = pika.URLParameters('amqps://user:password@localhost/user')
params.socket_timeout = 5
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='test_q')
body = 'Hello World'

for x in range(200):
    channel.basic_publish(exchange='', routing_key='test_q', body=body + str(x) + '!')
    print(" [x] Sent 'Hello World!'")

connection.close()
