# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:14:44 2020

@author: vibertvg
"""
import mykey
import pika
import os

# Configure a connexion to a remote RabbitMQ instance:
amqp_url= mykey.cloudlink
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5
#initiate the connexion
connection = pika.BlockingConnection(params) # Connect to CloudAMQP

channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch,method,properties, body):
    print(" [x] Received %r" % body)
    
channel.basic_consume(queue='hello',
                      on_message_callback=callback,auto_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
