# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 11:48:21 2020

@author: dormoyc
"""

import argparse
import pika
import mykeys

import time

amqpurl = mykeys.cloudamqplink
myQueue = "myWorkingQueue"

def callback(ch, method, properties, body):
    print (" [x] Received %r" % body)
       


    
    
connection = pika.BlockingConnection(pika.URLParameters(amqpurl))
channel = connection.channel()
    
channel.exchange_declare(exchange='logs',
                             exchange_type='fanout')
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
    
channel.queue_bind(exchange='logs',
                   queue=myQueue)

channel.basic_consume(callback,
                      queue=myQueue,
                      no_ack=True)