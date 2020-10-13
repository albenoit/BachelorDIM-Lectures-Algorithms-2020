# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:53:05 2020

@author: cuvellin
"""

import config
import pika
import os

url = os.environ.get('CLOUDAMQP_URL', config.amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params)

channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello Word!')
print(" [x] Sent 'Hello World !'")
connection.close()