# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:43:47 2020

@author: vibertvg
"""


import argparse
import mykey
import pika
import os
import simple_queue_publish
import simple_queue_read

parser= argparse.ArgumentParser(description="How to")
parser.add_argument('-read', action='store_true')
flags = parser.parse_args()

#flags.read = True

amqp_url= mykey.cloudlink
url = os.environ.get('CLOUDAMQP_URL', amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='hello')


#Test pour savoir le type d'exucution à effectuer
if flags.read:
    simple_queue_read.simple_queue_read(channel, connection)
else:
    simple_queue_publish.simple_queue_publish(channel, connection)


connection.close()
