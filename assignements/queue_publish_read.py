# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:24:18 2020
@author: tapiev
"""

import argparse
import pika

count = 0

import myKeysCloudAMQP
import os

amqp_url= myKeysCloudAMQP.cloud_amqp_key
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)

        
def publish(message,concurencebool):
    """
    this function upload a message on a queue 
    Params:
        message: a string that will be uploaded 
    """
    
    default_message="Hey"
    if message != "" and message != None :
        default_message = message

    connection = pika.BlockingConnection(params)
    channel=connection.channel()
    channel.queue_declare(queue='hello')
    if concurencebool :
         channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=str(default_message),
                          properties=pika.BasicProperties(delivery_mode=2))
         print("Pouet ")
    else:
        channel.basic_publish(exchange='',
                              routing_key='hello',
                              body=str(default_message))
    print("[x] Sent "+str(default_message))
    connection.close()

def read():
    """
    this fuction wait and consume a message snded on a queue
    """
    def callback(ch,method,properties,body):
        print(" [x] Received %r" % body)
        global count
        count +=1
        print("number of received event : " + str(count))
    print(amqp_url)
    connection = pika.BlockingConnection(params)
    channel=connection.channel()
    channel.queue_declare(queue='hello')    
    
    channel.basic_consume(queue='hello',
                          on_message_callback = callback,
                          auto_ack=True)
    print(' [*] Waiting for messages. o exit press CTRL+C')
    channel.start_consuming()
    
    
parser = argparse.ArgumentParser()
parser.add_argument('-read', action='store_true')
parser.add_argument('-m')
parser.add_argument('-concurrency', action='store_true')
args = parser.parse_args()
if args.read :
    read()
else:
    publish(args.m,args.concurrency)
    
    
    """ test """