# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:33:27 2020

@author: cuvellin
"""

import config, pika, os, argparse, simple_queue_publish, simple_queue_read

parser = argparse.ArgumentParser("How to")
parser.add_argument("-read",help="read messages", action="store_true")
parser.add_argument("-concurrency",help="multiple concurrent queue readers", action="store_true")
args = parser.parse_args()

url = os.environ.get('CLOUDAMQP_URL', config.amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params)

channel = connection.channel() # start a channel

if args.concurrency:
    queue = channel.queue_declare("task_queue", durable=True)
    channel.basic_qos(prefetch_count=1)
else:
    queue = channel.queue_declare(queue='hello')
    
    
if args.read:
    simple_queue_read.read(channel, queue.method.queue)
else :
    simple_queue_publish.publish(channel, queue.method.queue)
    
    
connection.close()