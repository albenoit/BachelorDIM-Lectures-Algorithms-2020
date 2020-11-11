# -*- coding: utf-8 -*-
#!/usr/bin/en python
import pika
import os
import config
import argparse

"""
Created on Tue Oct 13 13:47:56 2020

@author: fuchsca
"""

parser = argparse.ArgumentParser(description = 'Currency')
parser.add_argument('-concurrency');
url = os.environ.get('CLOUDAMQP_URL',config.amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 600

connection = pika.BlockingConnection(params) # Connect to CloudAMQPchannel = connection.channel()
channel = connection.channel()
nomMessage = "task_queue"
#corpsmessage = input('Entrez un message : ')
corpsmessage = 'TestMessage'
channel.queue_declare(queue=nomMessage,durable =True)
#channel.queue_declare(queue=nomMessage)


for i in range(1,10) :
    
    channel.basic_publish(exchange='',
                          routing_key=nomMessage,
                          body=corpsmessage,
                          properties=pika.BasicProperties(delivery_mode = 2,) # make message persistent
                        )
    print(" [X] Sent " + corpsmessage)


connection.close()