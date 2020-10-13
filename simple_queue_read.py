# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:24:16 2020

@author: lentzye
"""
import mykeys
import pika, os


url = os.environ.get('CLOUDAMQP_URL', mykeys.cloudampqlink)
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue
def callback(ch, method, properties, body):
  print(" [x] Received " + str(body))

channel.basic_consume('hello',
                      callback,
                      auto_ack=True)

print(' [*] Waiting for messages:')
channel.start_consuming()
connection.close()