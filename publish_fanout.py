# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 11:35:30 2020

@author: polletb
"""
def publish_queue_fanout(channel):
    '''
    Publish to RabbitMQ Advanced Message Queuing with Pika
    Parameters:
            check official documentation : https://pika.readthedocs.io/en/stable/
    '''
    channel.exchange_declare(exchange='logs',
                             exchange_type='fanout')

    channel.basic_publish(exchange='logs',
                          routing_key='',
                          body='Hello World! Fanout')

    print(" [x] Sent 'Hello World! Fanout'")