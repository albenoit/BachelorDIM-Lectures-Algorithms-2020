# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:37:35 2020

@author: lentzye
"""

import pika, os
import mykeys
import argparse

url = os.environ.get('CLOUDAMQP_URL', mykeys.cloudampqlink)
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel=connection.channel()
channel.queue_declare(queue='hello')

def publish_queue():
    
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello CloudAMQP!')
    print (" [x] Sent 'Hello World'")
    connection.close()
    
def read_queue():
    def callback(ch, method, properties, body):
      print(" [x] Received " + str(body))
    
    channel.basic_consume('hello',
                          callback,
                          auto_ack=True)
    
    print(' [*] Waiting for messages:')
    channel.start_consuming()
    connection.close()


parser = argparse.ArgumentParser(description='How to')
parser.add_argument('-read', action='store_true')
flags=parser.parse_args()

if(flags.read):
    read_queue()
else :
    publish_queue()
    
connection.close
