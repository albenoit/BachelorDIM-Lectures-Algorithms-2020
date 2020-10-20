# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:03:45 2020

@author: vibertvg
"""

   
    
def publish_queue(channel, queueName:str):
    '''
    Publish to RabbitMQ Advanced Message Queuing with Pika
    Parameters:
            check official documentation : https://pika.readthedocs.io/en/stable/
            queueName: str
    '''
    channel.basic_publish(exchange='',
                          routing_key=queueName,
                          body='Hello World!')
    
    print(" [x] Sent 'Hello World!'")