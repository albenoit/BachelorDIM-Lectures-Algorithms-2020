# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:29:03 2020

@author: bouvaran
"""
import mykeys
import pika
AMQP_URL = mykeys.cloudamplink

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
