# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 11:43:56 2020

@author: dormoyc
"""

import pika
import mykeys

amqpurl = mykeys.cloudamqplink

connection = pika.BlockingConnection(pika.URLParameters(amqpurl))
channel = connection.channel()
channel.queue_declare(queue='myWorkingQueue', durable=True)

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

channel.basic_publish(exchange='logs',
                      routing_key='',
                      body='Hello World! Bonjour tout le monde!')

print(" [x] Sent 'Hello World!'")
connection.close()