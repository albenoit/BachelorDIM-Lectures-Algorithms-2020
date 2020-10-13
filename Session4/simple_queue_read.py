# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:13:54 2020

@author: vcouttmp
"""

import pika
import mykeys

amqpurl = mykeys.cloudamqplink

connection = pika.BlockingConnection(pika.URLParameters(amqpurl))
channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print (" [x] Received %r" % body)
    
channel.basic_consume(queue='hello',
                      on_message_callback = callback,
                      auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()