# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:51:30 2020

@author: bouvaran
"""
import mykeys
import pika
import argparse
AMQP_URL = mykeys.cloudamplink

parser = argparse.ArgumentParser(description= "How to")
parser.add_argument('-read',action='store_true')
FLAGS=parser.parse_args()

if FLAGS.read:
    connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
    channel = connection.channel() 
    channel.queue_declare(queue='presentation’')
    
    def callback(ch, method, properties, body):
        print(" [Antoine_le_bg] Received %r" % body)

    channel.basic_consume(queue = 'presentation’',
                          on_message_callback = callback,
                          auto_ack=True)
    print(' [Antoine_le_bg] Waiting for messages: to exit press ctrl+c')
    channel.start_consuming()
    
else:    
    connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
    channel = connection.channel()
    channel.queue_declare(queue='presentation’')
    
    channel.basic_publish(exchange='',
                         routing_key='presentation’',
                         body='Hello World!')
    print("[Antoine_le_bg] salut la pleb")
    connection.close()

