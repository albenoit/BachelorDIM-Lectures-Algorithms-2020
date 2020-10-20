# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:03:07 2020

@author: lentzye
"""
import mykeys
import pika, os
import argparse

url = os.environ.get('CLOUDAMQP_URL', mykeys.cloudampqlink)
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)

channel=connection.channel()
channel.queue_declare(queue='Coucou',durable=True)

parser = argparse.ArgumentParser(description='How to')
parser.add_argument('-concurrency', action='store_true')
flags=parser.parse_args()

if(flags.concurrency):
    channel.basic_publish(exchange='',
                      routing_key="Coucou",
                      body='Persistentation of un message',
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
    print (" [x] Sentahahah 'Hello World'")    

else :
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello CloudAMQP!')
    print (" [x] Sent 'Hello World'")    

connection.close()