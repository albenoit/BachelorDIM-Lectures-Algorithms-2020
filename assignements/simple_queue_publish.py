# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:55:28 2020

@author: bouvaran
"""

import mykeys
import pika

AMQP_URL = mykeys.cloudamplink

connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                     routing_key='hello',
                     body='Hello World!')
print("[x] Sent 'Hello World!")
connection.close()