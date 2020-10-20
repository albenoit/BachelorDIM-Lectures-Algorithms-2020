# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:48:25 2020

@author: derbaghc
"""

import config
import pika
import os 
import argparse
import simple_queue_publish as publisher

url = os.environ.get('CLOUDAMQP_url', config.keyAMQP)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue='hello1', durable=True)
channel.basic_qos(prefetch_count=1)

parser = argparse.ArgumentParser(description="How to")
parser.add_argument('-concurrency', action='store_true')
FLAGS = parser.parse_args()

def callback(ch, method, properties, body):
    print(" [X] Received %r" %body)
    # TODO process the message
    print(" [X] Message Processed, acknowledging (to delete message from the queue)")
    ch.basic_ack(delivery_tag = method.delivery__tag)
        
    
def consume():
    channel.basic_consume(queue='hello1', 
                          on_message_callback=callback,
                          auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    
consume()