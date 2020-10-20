# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:47:52 2020

@author: derbaghc
"""

import config
import pika 
import os 

url = os.environ.get('CLOUDAMQP_url', config.keyAMQP)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(pika.URLParameters(config.keyAMQP))
channel = connection.channel()
channel.queue_declare(queue='hello1', durable=True)


def publish(queueName):
    #channel.exchange_declare(exchange='logs', 
     #                        exchange_type='fanout')
    channel.basic_publish(exchange='', 
                          routing_key=queueName,
                          body='Hello World', 
                          properties=pika.BasicProperties(
                                  delivery_mode = 2 
                          ))
    print(" [X] Sent 'Hello World!'")
    connection.close()