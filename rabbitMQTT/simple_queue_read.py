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

def callback(ch, method, properties,body) :
    print("[X] Received %r" %body)
    
channel.basic_consume(queue='MonMessage',
                      on_message_callback=callback,
                      auto_ack=True)
print(' [*] Waiting for messages. To Exit press CTRL + C')
channel.start_consuming()
connection.close()