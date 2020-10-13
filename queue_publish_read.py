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

AMQP_URL = config('AMQP_URL')

parser= argp.ArgumentParser(description="How to")
parser.add_argument('-read', action='store_true')
flags = parser.parse_args()

#flags.read = True

url = os.environ.get('CLOUDAMQP_URL', AMQP_URL)
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='hello')


#Test pour savoir le type d'exucution à effectuer
if flags.read:
    simple_queue_read.read_queue(channel)
else:
    simple_queue_publish.publish_queue(channel)
    

connection.close()

