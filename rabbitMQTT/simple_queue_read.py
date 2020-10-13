# -*- coding: utf-8 -*-
#!/usr/bin/en python
import pika

"""
Created on Tue Oct 13 13:54:57 2020

@author: fuchsca
"""


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch, method, properties,body) :
    print(" [X] Received %r" %body)
    
channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)
print(' [*] Waiting for messages. To Exit press CTRL + C')
channel.start_consuming()