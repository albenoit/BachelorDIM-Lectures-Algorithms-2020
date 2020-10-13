# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:52:37 2020

@author: polletb
"""
from decouple import config 
import pika
import os

AMQP_URL = config('AMQP_URL')

url = os.environ.get('CLOUDAMQP_URL', AMQP_URL)
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

print(" [x] Sent 'Hello World!'")
connection.close()