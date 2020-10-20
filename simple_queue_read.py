# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:24:16 2020

@author: lentzye
"""
import mykeys
import pika, os
import argparse

url = os.environ.get('CLOUDAMQP_URL', mykeys.cloudampqlink)
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='Coucou',durable=True) # Declare a queue
def callback(ch, method, properties, body):
  print(" [x] Received " + str(body))

parser = argparse.ArgumentParser(description='How to')
parser.add_argument('-concurrency', action='store_true')
flags=parser.parse_args()

if(flags.concurrency):  
    channel.basic_consume('Coucou',
                      callback,
                      auto_ack=False)
else :
    channel.basic_consume('hello',
                      callback,
                      auto_ack=True)


channel.start_consuming()
connection.close()