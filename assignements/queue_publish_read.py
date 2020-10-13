# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:33:27 2020

@author: cuvellin
"""

import config, pika, os, argparse, simple_queue_publish, simple_queue_read

parser = argparse.ArgumentParser("How to")
parser.add_argument("-read",help="read messages", action="store_true")
args = parser.parse_args()

url = os.environ.get('CLOUDAMQP_URL', config.amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params)

channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue

if args.read:
    simple_queue_read.read(channel)
else :
    simple_queue_publish.publish(channel)
connection.close()