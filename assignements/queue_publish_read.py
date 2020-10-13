# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:24:18 2020

@author: tapiev
"""

import argparse
import pika

count = 0
        
def publish(message):
    """
    this function upload a message on a queue 
    Params:
        message: a string that will be uploaded 
    """
    f = open("P:\\Git_algo\key.txt", "r")
    connec_string =f.read()
    f.close()
    
    connection = pika.BlockingConnection(pika.URLParameters(connec_string))
    channel=connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=str(message))
    print("[x] Sent 'Hello World'")
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
    f = open("P:\\Git_algo\key.txt", "r")
    connec_string = f.read()
    print(connec_string)
    connection = pika.BlockingConnection(pika.URLParameters(connec_string))
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
args = parser.parse_args()
if args.read :
    read()
else:
    publish(args.m)