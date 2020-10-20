# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:34:50 2020

@author: vcouttmp
"""

import argparse
import pika
import mykeys

import time

amqpurl = mykeys.cloudamqplink
myQueue = "hello"
myQueue = "myWorkingQueue"

count = 0

'''
Function which publish a message to amqp
@param str message, the message which it publish
'''
def publish(message,conq):
    connection = pika.BlockingConnection(pika.URLParameters(amqpurl))
    channel = connection.channel()
    channel.queue_declare(queue=myQueue, durable=True)
    
    if(conq):
      channel.basic_publish(exchange='',
                  routing_key=myQueue,
                  body=message,
                  properties = pika.BasicProperties(delivery_mode = 2))
      print("concurrency")
    else:
        #channel.basic_publish(exchange='',
        #                  routing_key='hello',
        #                  body=message)
        
        channel.basic_publish(exchange='',
                          routing_key=myQueue, #Nom de la queue dans CloudAMQP
                          body=message,
                          properties=pika.BasicProperties(
                          delivery_mode = 2, # make message persistent
                          ))
        
    print(" [x] Sent 'Hello World!'")
    connection.close()

'''
Function which display a message from the queue
'''
def callback(ch, method, properties, body):
    print (" [x] Received %r" % body)
    
    print(" [X] Message Processed, acknowledging (to delete message from the queue")
    ch.basic_ack(delivery_tag = method.delivery_tag)
    
    global count
    count+=1
    print ('message lu : ', count)
    
    time.sleep(5)
    
'''
Function which is going to read every messages in queue
'''
def read():    
    connection = pika.BlockingConnection(pika.URLParameters(amqpurl))
    channel = connection.channel()
    channel.queue_declare(queue=myQueue, durable=True)

    channel.basic_consume(queue=myQueue,
                          on_message_callback = callback,
                          auto_ack=False) #False quand on fait le multiple reader
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    
    channel.basic_qos(prefetch_count=1) #Garde au minimum 1 message dans le cache
    channel.start_consuming()



parser = argparse.ArgumentParser(description= "How to")
parser.add_argument('-read', action='store_true')
parser.add_argument('-m')
parser.add_argument('-concurrency', action='store_true')
FLAGS = parser.parse_args()

if(FLAGS.read):
    read()
else:
    publish(FLAGS.m, FLAGS.concurrency)