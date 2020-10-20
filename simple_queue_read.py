# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:06:29 2020

@author: polletb
"""

def callback(ch, method, properties, body):
    '''
    Callback for read message
    Parameters:
            check official documentation : https://pika.readthedocs.io/en/stable/
    '''
    print(" [" + str(method.delivery_tag) + "] Received " + str(body))


def read_queue(channel):
    '''
    Read RabbitMQ Advanced Message Queuing with Pika
    Parameters:
            check official documentation : https://pika.readthedocs.io/en/stable/
    '''
    channel.basic_consume('hello',
                      callback,
                      auto_ack=True)

    print(' [*] Waiting for messages:')
    channel.start_consuming()




