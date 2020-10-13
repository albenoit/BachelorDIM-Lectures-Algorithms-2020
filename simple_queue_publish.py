# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:03:07 2020

@author: lentzye
"""
import mykeys
import pika, os

url = os.environ.get('CLOUDAMQP_URL', mykeys.cloudampqlink)
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)

channel=connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello CloudAMQP!')
print (" [x] Sent 'Hello World'")
connection.close()