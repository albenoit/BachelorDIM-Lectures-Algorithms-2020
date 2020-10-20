# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:48:21 2020

@author: polletb
"""
from decouple import config 
import argparse as argp
import pika
import os
import simple_queue_publish
import simple_queue_read

'''
Use Python-decouple for .env file
'''
AMQP_URL = config('AMQP_URL')

'''
Use argparse to add argument before execution
'''
parser = argp.ArgumentParser(description="How to")
parser.add_argument('-read', action='store_true')
parser.add_argument('-concurrency', action='store_true')
flags = parser.parse_args()

'''
Connect params to cloudAMQP with Pika
'''
url = os.environ.get('CLOUDAMQP_URL', AMQP_URL)
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params)

'''
Test type channel with argument
'''
queueName = "task_queue"

channel = connection.channel()
if flags.concurrency and flags.read:
    channel.queue_declare(queue=queueName, durable=True)
    channel.basic_qos(prefetch_count=10)
elif flags.concurrency:
    channel.queue_declare(queue=queueName, durable=True)
else:
    channel.queue_declare(queue=queueName)
    #print(queue.method.queue)

'''
Test for argument
'''
if flags.read:
    simple_queue_read.read_queue(channel, queueName)
else:
    for i in range(0, 100):
        simple_queue_publish.publish_queue(channel, queueName)
    

connection.close()

