# -*- coding: utf-8 -*-
#!/usr/bin/en python
import pika
import os
import config

"""
Created on Tue Oct 13 13:54:57 2020

@author: fuchsca
"""



url = os.environ.get('CLOUDAMQP_URL',config.amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQPchannel = connection.channel()
channel = connection.channel()
channel.queue_declare(queue='MonMessage')

#Reception
counter = 0

def callback(ch, method, properties,body) :
    global counter
    counter = counter + 1
    print(" [X] Received %r" %body + "il y a eu %r messages" %counter)
    
    print("[X] Message Processed, acknoledging(to delete message from queue)")
    ch.basic_ack(delivery_tag = method.delivery_tag)
    
channel.basic_consume(queue='MonMessage',
                      on_message_callback=callback,
                      auto_ack=False)

#print(' [*] Waiting for messages. To Exit press CTRL + C')

channel.start_consuming()
connection.close()