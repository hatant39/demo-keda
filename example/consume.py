#!/usr/bin/env python

import pika, time

params = pika.URLParameters('amqps://user:password@localhost/user')
params.socket_timeout = 5
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='test_q')

def test_process_function(msg):
  print(" Test processing")
  print(" [x] Received " + str(msg))

  time.sleep(5) # delays for 5 seconds
  print(" Test processing finished");
  return;

# create a function which is called on incoming messages
def callback(ch, method, properties, body):
  test_process_function(body)

# set up subscription on the queue
channel.basic_consume('test_q',
  callback,
  auto_ack=True)

# start consuming (blocks)
channel.start_consuming()
connection.close()
