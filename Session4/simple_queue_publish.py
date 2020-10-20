# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:45:21 2020

@author: vcouttmp
"""

import pika
import mykeys

amqpurl = mykeys.cloudamqplink

connection = pika.BlockingConnection(pika.URLParameters(amqpurl))
channel = connection.channel()
channel.queue_declare(queue='myWorkingQueue', durable=True)

channel.basic_publish(exchange='',
                      routing_key='myWorkingQueue',
                      body='Hello World! Bonjour tout le monde!',
                      properties = pika.BasicProperties(delivery_mode = 2))

print(" [x] Sent 'Hello World!'")
connection.close()