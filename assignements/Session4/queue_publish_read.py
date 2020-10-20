# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:56:25 2020

@author: derbaghc
"""

import config
import pika
import os 
import argparse
import simple_queue_read as reader
import simple_queue_publish as publisher

url = os.environ.get('CLOUDAMQP_url', config.keyAMQP)
params = pika.URLParameters(url)
params.socket_timeout = 5


connection = pika.BlockingConnection(params)
channel = connection.channel()
queueName = 'hello1'
channel.queue_declare(queue=queueName, durable=True)

parser = argparse.ArgumentParser(description="Persistent message")
#parser.add_argument('-read', action='store_true')
parser.add_argument('-concurrency', action='store_true')
FLAGS = parser.parse_args()

def callback(ch, method, properties, body):
    print(" [X] Received %r" %body)

#read correspond au add_argument
if FLAGS.concurrency:
    reader.consume(queueName)
else:
    publisher.publish(queueName)
    

    
