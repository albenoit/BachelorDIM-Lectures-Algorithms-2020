# -*- coding: utf-8 -*-
#!/usr/bin/en python
import pika
import os
import config

"""
Created on Tue Oct 13 13:47:56 2020

@author: fuchsca
"""


url = os.environ.get('CLOUDAMQP_URL',config.amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQPchannel = connection.channel()
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [X] Sent 'Hello World!'")


connection.close()