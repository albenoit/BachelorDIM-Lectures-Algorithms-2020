# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:56:25 2020

@author: derbaghc
"""

import config
import pika
import os 
import argparse
import simple_queue_read as reader
import simple_queue_publish as publisher

#Connexion à Cloud AMQP
url = os.environ.get('CLOUDAMQP_url', config.keyAMQP)
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(pika.URLParameters(config.keyAMQP))

baba = pika.BlockingConnection(params)
channel = connection.channel()

'''
#Partie Concurrency

channel.queue_declare(queue='hello1', durable=True)
channel.basic_qos(prefetch_count=1)
'''

#queueName = 'hello1'

##One messages to many queue
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')
result = channel.queue_declare(queue='', exclusive=True)
queueName = result.method.queue
channel.queue_bind(exchange='logs',
                   queue=queueName)

##Arguments
parser = argparse.ArgumentParser(description="Persistent message")
#arser.add_argument('-concurrency', action='store_true')
parser.add_argument('-read', action='store_true')
FLAGS = parser.parse_args()

#read correspond au add_argument
if FLAGS.read:
    reader.consume(channel, queueName)
else:
    publisher.publish(channel, queueName, connection)

    

    
