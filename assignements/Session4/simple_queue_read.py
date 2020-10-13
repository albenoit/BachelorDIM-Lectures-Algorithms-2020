# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:48:25 2020

@author: derbaghc
"""

import config
import pika
import os 

url = os.environ.get('CLOUDAMQP_url', config.keyAMQP)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [X] Received %r" %body)
    
channel.basic_consume(queue='hello', 
                      on_message_callback=callback,
                      auto_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()