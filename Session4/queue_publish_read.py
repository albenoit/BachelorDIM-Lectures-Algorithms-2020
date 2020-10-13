# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:34:50 2020

@author: vcouttmp
"""

import argparse
import pika
import mykeys

amqpurl = mykeys.cloudamqplink

count = 0

'''
Function which publish a message to amqp
@param str message, the message which it publish
'''
def publish(message):
    connection = pika.BlockingConnection(pika.URLParameters(amqpurl))
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
    print(" [x] Sent 'Hello World!'")
    connection.close()

'''
Function which display a message from the queue
'''
def callback(ch, method, properties, body):
    print (" [x] Received %r" % body)
    global count
    count+=1
    print ('message lu : ', count)
    
'''
Function which is going to read every messages in queue
'''
def read():    
    connection = pika.BlockingConnection(pika.URLParameters(amqpurl))
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    channel.basic_consume(queue='hello',
                          on_message_callback = callback,
                          auto_ack=True)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()



parser = argparse.ArgumentParser(description= "How to")
parser.add_argument('-read', action='store_true')
parser.add_argument('-m')
FLAGS = parser.parse_args()

if(FLAGS.read):
    read()
else:
    publish(FLAGS.m)